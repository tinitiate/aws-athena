import gzip
import boto3
import pyarrow as pa


# #########################################################
# Bytes Compression and return compressed object (NOT FILE)
# #########################################################

# compression (Gzip)
def compress_gz_data(p_input_bytes):
    gz_data = gzip.compress(p_input_bytes)
    return gz_data

# compression (Snappy)
def compress_snappy_data(p_input_bytes):
    compressed_parquet_data = pa.compress(p_input_bytes, codec='snappy')
    return compressed_parquet_data


# #########################################################
# AWS Operations
# #########################################################

# Function to upload data to S3
def aws_s3_upload(p_data_bytes, p_s3_bucket, p_s3_folder, p_filename, p_aws_profile):
    session = boto3.Session(profile_name=p_aws_profile)
    s3 = session.client('s3')
    key = f"{p_s3_folder}/{p_filename}"
    s3.put_object(Body=p_data_bytes, Bucket=p_s3_bucket, Key=key)
