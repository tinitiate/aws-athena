import pyarrow.parquet as pq

table = pq.read_table("D:/code/tinitiate-git-master/aws-athena/code/aws-s3-data-generator/data.parquet")
print(table.schema)