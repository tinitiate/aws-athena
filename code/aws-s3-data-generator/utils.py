import gzip
import bz2
import boto3
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
import io
import json
from io import BytesIO
import csv

# #########################################################
# Bytes Compression and return compressed object (NOT FILE)
# #########################################################

# compression (Gzip)
def compress_gz_data(p_input_bytes):
    gz_data = gzip.compress(p_input_bytes)
    return gz_data

# compression (Snappy)
def compress_snappy_data(p_input_bytes):
    compressed_parquet_data = pa.compress(p_input_bytes, asbytes=True, codec='snappy')
    return compressed_parquet_data


# ########################################################
# AWS IO Functions
# ########################################################

# ########################
# JSON Output
# ########################
def write_dict_to_json_and_upload_to_s3(p_dict_data, p_s3_bucket,p_s3_folder, p_filename, p_aws_profile):
    # Convert dictionary to JSON string
    json_data = json.dumps(p_dict_data)
    # Create a BytesIO object
    output_stream = BytesIO()
    output_stream.write(json_data.encode())
    output_stream.seek(0)
    # Initialize S3 client
    session = boto3.Session(profile_name=p_aws_profile)
    s3_client = session.client('s3')
    s3_key = f"{p_s3_folder}/{p_filename}"
    # Upload to S3
    s3_client.upload_fileobj(output_stream, p_s3_bucket, s3_key)


def write_list_to_json_and_upload_to_s3(p_list_data, p_s3_bucket,p_s3_folder, p_filename, p_aws_profile):
    # Convert list to JSON string
    json_data = json.dumps(p_list_data)
    # Create a BytesIO object
    output_stream = BytesIO()
    output_stream.write(json_data.encode())
    output_stream.seek(0)
    # Initialize S3 client
    session = boto3.Session(profile_name=p_aws_profile)
    s3_client = session.client('s3')
    s3_key = f"{p_s3_folder}/{p_filename}"
    # Upload to S3
    s3_client.upload_fileobj(output_stream, p_s3_bucket, s3_key)


def write_list_to_ndjson_and_upload_to_s3(p_list_data, p_s3_bucket, p_s3_folder, p_filename, p_aws_profile):
    # Create a BytesIO object
    output_stream = BytesIO()
    # Convert each item in the list to a JSON string and write to the BytesIO object
    for item in p_list_data:
        json_data = json.dumps(item) + "\n"
        output_stream.write(json_data.encode())
    # Move back to the start of the BytesIO object
    output_stream.seek(0)
    # Initialize S3 client
    session = boto3.Session(profile_name=p_aws_profile)
    s3_client = session.client('s3')
    s3_key = f"{p_s3_folder}/{p_filename}"
    # Upload to S3
    s3_client.upload_fileobj(output_stream, p_s3_bucket, s3_key)


# ########################
# CSV Output
# ########################
def write_list_to_csv_and_upload_to_s3(p_list_data, p_s3_bucket, p_s3_folder, p_filename, p_aws_profile, p_compression='Compress'):
    if not p_list_data:
        raise ValueError("The provided list is empty")

    # Create an in-memory text stream
    output = io.StringIO()
    l_fieldnames = p_list_data[0].keys()
    
    # Create a CSV writer object
    writer = csv.DictWriter(output, fieldnames=l_fieldnames)
    
    # Write the header and data
    writer.writeheader()
    writer.writerows(p_list_data)
    
    # Move to the beginning of the StringIO object
    output.seek(0)
    data = output.getvalue()

    # Compress the CSV data
    l_filename = p_filename
    if p_compression.lower() == 'bz2':
        compressor = bz2.BZ2Compressor()
        compressed_data = compressor.compress(data.encode()) + compressor.flush()
        l_filename += '.bz2'
    elif p_compression.lower() == 'gz':
        compressed_data = gzip.compress(data.encode())
        l_filename += '.gz'
    else:
        compressed_data = data.encode()

    # Initialize S3 client
    session = boto3.Session(profile_name=p_aws_profile)
    s3_client = session.client('s3')
    s3_key = f"{p_s3_folder}/{l_filename}"
    
    # Upload compressed data to S3
    s3_client.put_object(Body=compressed_data, Bucket=p_s3_bucket, Key=s3_key)


def write_dict_to_csv_and_upload_to_s3(p_dict_data, p_s3_bucket, p_s3_folder, p_filename, p_aws_profile, p_compression='Compress'):
    # Create an in-memory text stream
    output = io.BytesIO()   
    # Create a CSV writer object
    writer = csv.DictWriter(output.getvalue(), fieldnames=p_dict_data[0].keys())
    # Write the header
    writer.writeheader()
    # Write the dictionary data
    writer.writerows(p_dict_data)
    # Move to the beginning of the StringIO object
    output.seek(0)

    # Compress the CSV data
    l_filename = p_filename
    if p_compression.lower() == 'bz2':
        compressor = bz2.BZ2Compressor()
        output = compressor.compress(output.getvalue()) + compressor.flush()
        l_filename = p_filename + '.bz2'
    elif p_compression.lower() == 'gz':
        compressor = gzip.compress
        output = compressor(output.getvalue())
        l_filename = p_filename + '.gz'

    # Initialize S3 client
    session = boto3.Session(profile_name=p_aws_profile)
    s3_client = session.client('s3')
    s3_key = f"{p_s3_folder}/{l_filename}"
    # Upload to S3
    s3_client.put_object(Body=output.getvalue(), Bucket=p_s3_bucket, Key=s3_key)

# ########################
# PARQUET Output
# ########################
# Write file to AWS S3
def write_list_to_parquet_and_upload_to_s3(p_list_data, p_s3_bucket, p_s3_folder, p_filename, p_aws_profile, p_compression='Compress'):
    # Ensure that p_list_data is a list of dictionaries, each representing an order
    if not p_list_data or not isinstance(p_list_data[0], dict):
        raise ValueError("Input data is not in the expected format of a list of dictionaries.")

    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(p_list_data)

    # Create a Parquet table from the DataFrame
    table = pa.Table.from_pandas(df, preserve_index=False)

    # Write the Parquet table to a BytesIO object with specified compression
    output_stream = BytesIO()
    pq.write_table(table, output_stream, compression=p_compression)
    output_stream.seek(0)

    # Upload to AWS S3
    session = boto3.Session(profile_name=p_aws_profile)
    s3_client = session.client('s3')
    s3_key = f"{p_s3_folder}/{p_filename}"
    s3_client.upload_fileobj(output_stream, p_s3_bucket, s3_key)

    # return f"File uploaded to s3://{p_s3_bucket}/{s3_key}"


def write_dict_to_parquet_and_upload_to_s3(p_dict_data, p_s3_bucket, p_s3_folder, p_filename, p_aws_profile, p_compression='Compress'):
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame([p_dict_data])
    # Create a Parquet table from the DataFrame
    table = pa.Table.from_pandas(df)
    # Write the Parquet table to a BytesIO object
    output_stream = BytesIO()
    pq.write_table(table, output_stream, compression=p_compression)
    output_stream.seek(0)
    # Upload to AWS S3
    session = boto3.Session(profile_name=p_aws_profile)
    s3_client = session.client('s3')
    s3_key = f"{p_s3_folder}/{p_filename}"
    s3_client.upload_fileobj(output_stream, p_s3_bucket, s3_key)
    # return f"File uploaded to s3://{p_s3_bucket}/{s3_key}"


# ########################################################
# Local Drive IO Functions
# ########################################################
def local_list_to_parquet(p_list_data, p_file_path):
    df = pd.DataFrame(p_list_data)
    df.to_parquet(p_file_path)

def local_dict_to_parquet(p_list_data, p_file_path):
    df = pd.DataFrame(p_list_data)
    df.to_parquet(p_file_path)

def local_list_to_json(p_list_data, p_file_path):
    df = pd.DataFrame(p_list_data)
    df.to_parquet(p_file_path)

def local_dict_to_json(p_list_data, p_file_path):
    df = pd.DataFrame(p_list_data)
    df.to_parquet(p_file_path)

def local_list_to_csv(p_list_data, p_file_path):
    df = pd.DataFrame(p_list_data)
    df.to_parquet(p_file_path)

def local_dict_to_csv(p_list_data, p_file_path):
    df = pd.DataFrame(p_list_data)
    df.to_parquet(p_file_path)

# #########################################################
# MISC Functions
# #########################################################
# Function to upload data to S3
def aws_s3_upload(p_data_bytes, p_s3_bucket, p_s3_folder, p_filename, p_aws_profile):
    session = boto3.Session(profile_name=p_aws_profile)
    s3 = session.client('s3')
    key = f"{p_s3_folder}/{p_filename}"
    s3.put_object(Body=p_data_bytes, Bucket=p_s3_bucket, Key=key)

def dict_to_csvbytes(p_dict_data):
    # Create an in-memory text stream
    output = io.StringIO()
    # Create a CSV writer object
    writer = csv.DictWriter(output, fieldnames=p_dict_data[0].keys())
    # Write the header
    writer.writeheader()
    # Write the dictionary data
    writer.writerows(p_dict_data)
    # Get the CSV data as a string
    csv_string = output.getvalue()
    # Encode the string to bytes
    csv_bytes = csv_string.encode()

    return csv_bytes
