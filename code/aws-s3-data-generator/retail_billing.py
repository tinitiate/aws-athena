from faker import Faker
from datetime import datetime, timedelta
import json
import random
import io
import pandas as pd
import utils as u

# Initialize Faker for generating fake data
fake = Faker()

# Function to generate a random date within a specific range
def random_date(start_date, end_date):
    return fake.date_time_between_dates(datetime_start=start_date, datetime_end=end_date)

# Function to generate a retail billing dataset
def generate_orderdata_dict():

    order = {
        "order_id": fake.random_int(min=1000, max=9999),
        "store_id": fake.random_int(min=1, max=20),
        "order_date": random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)).strftime('%Y-%m-%dT%H:%M:%S'),
        "customer": {
            "customer_id": fake.random_int(min=100, max=999),
            "name": fake.name(),
            "email": fake.email()
        },
        "items": []
    }

    for _ in range(fake.random_int(min=1, max=5)):
        item = {
            "product_id": fake.random_int(min=1, max=25),
            "product_name": fake.word(),
            "quantity": fake.random_int(min=1, max=10),
            "price": round(random.uniform(5.0, 50.0), 2)
        }
        order["items"].append(item)

    return order

    if output_format.lower() == 'parquet':
        # Convert to Parquet using pandas
        parquet_data = pd.json_normalize(order)
        parquet_bytes_io = io.BytesIO()
        parquet_data.to_parquet(parquet_bytes_io, index=False)
        # with open("D:/code/tinitiate-git-master/aws-athena/code/aws-s3-data-generator/data.parquet", 'wb') as file:  # Open file in write-binary mode
        #    file.write(parquet_bytes_io.getvalue())
        parquet_bytes_io.seek(0)
        return parquet_bytes_io.getvalue()
    else:
        # Default is JSON format
        return json.dumps(order)

    # if output_format.lower() == 'csv':
    #     # Convert to CSV using pandas
    #     csv_data = pd.json_normalize(billing_data['orders'])
    #     csv_bytes = csv_data.to_csv(index=False).encode('utf-8')
    #     return csv_bytes


# Function to generate a retail billing dataset
def generate_billing_compressed_bytes(num_bills, output_format='json', compresson='gzip'):

    compressed_data = ""
    data_bytes = generate_orderdata_parquet_json_bytes(num_bills, output_format)

    if output_format=='json':
        data_bytes = data_bytes.encode('utf-8')

    if compresson.lower() == 'gz':
        compressed_data = u.compress_gz_data(data_bytes)
    if compresson.lower() == 'snappy':
        compressed_data = u.compress_snappy_data(data_bytes)
    
    return compressed_data


def billing_data_to_local_storage(p_s3_folder, p_filename, output_format, compresson=None):
    if compresson:
        data_bytes = generate_billing_compressed_bytes(num_bills, output_format,compresson)
        u.aws_s3_upload(data_bytes, p_s3_bucket, p_s3_folder, p_filename, p_aws_profile)
    else:
        data_bytes = generate_billing_compressed_bytes(num_bills, output_format)
        u.aws_s3_upload(data_bytes, p_s3_bucket, p_s3_folder, p_filename, p_aws_profile)



def billing_data_to_s3(p_s3_bucket, p_s3_folder, p_filename, p_aws_profile, num_bills, output_format, compresson=None):
    if compresson:
        data_bytes = generate_billing_compressed_bytes(num_bills, output_format,compresson)
        u.aws_s3_upload(data_bytes, p_s3_bucket, p_s3_folder, p_filename, p_aws_profile)
    else:
        data_bytes = generate_billing_compressed_bytes(num_bills, output_format)
        u.aws_s3_upload(data_bytes, p_s3_bucket, p_s3_folder, p_filename, p_aws_profile)
