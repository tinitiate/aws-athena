import retail_billing as rb
from datetime import datetime


# Variables
l_aws_profile = 'admin'           # AWS Profile
l_s3_bucket = 'ti-p-data'         # AWS Bucket
l_num_bills = 1000

"""
# CSV
l_s3_folder = 'customer-billing/csv'  # AWS Bucket-Folder
l_output_format = "CSV"
l_compresson = None
l_filename = "invoice_"+datetime.now().strftime('%Y%m%d%H%M%S')+"."+l_output_format.lower()
"""
"""
# CSV-GZ
l_s3_folder = 'customer-billing/gz-csv'  # AWS Bucket-Folder
l_output_format = "CSV"
l_compresson = "gz"
l_filename = "invoice_"+datetime.now().strftime('%Y%m%d%H%M%S')+"."+l_output_format.lower()+"."+l_compresson.lower()
"""
"""
# JSON
l_s3_folder = 'customer-billing/json'  # AWS Bucket-Folder
l_output_format = "json"
l_compresson = None
l_filename = "invoice_"+datetime.now().strftime('%Y%m%d%H%M%S')+"."+l_output_format.lower()
"""

# JSON-GZ
l_s3_folder = 'customer-billing/gz-json'  # AWS Bucket-Folder
l_output_format = "json"
l_compresson = "gz"
l_filename = "invoice_"+datetime.now().strftime('%Y%m%d%H%M%S')+"."+l_output_format.lower()+"."+l_compresson.lower()

"""
# PARQUET
l_s3_folder = 'customer-billing/parquet'  # AWS Bucket-Folder
l_output_format = "PARQUET"
l_compresson = None
l_filename = "invoice_"+datetime.now().strftime('%Y%m%d%H%M%S')+"."+l_output_format.lower()
"""
"""
# PARQUET-snappy
l_s3_folder = 'customer-billing/snappy-parquet'  # AWS Bucket-Folder
l_output_format = "PARQUET"
l_compresson = "gz"
l_filename = "invoice_"+datetime.now().strftime('%Y%m%d%H%M%S')+"."+l_output_format.lower()+"."+l_compresson.lower()
"""

rb.billing_data_to_s3( p_s3_bucket = l_s3_bucket
                      ,p_s3_folder = l_s3_folder
                      ,p_filename = l_filename
                      ,p_aws_profile = l_aws_profile
                      ,num_bills = l_num_bills
                      ,output_format = l_output_format
                      ,compresson = l_compresson)
