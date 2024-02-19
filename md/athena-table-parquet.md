# Creating Athena tables with PARQUET files
* Parquet is a columnar storage file format that is optimized for use with big data processing frameworks. It is widely used in data engineering and big data ecosystems, particularly with tools like Apache Hadoop, Apache Spark, and Apache Drill. Here are some key aspects of Parquet:
* Columnar Storage: Unlike row-based storage formats, Parquet stores data column-wise. This means each column of data is stored together, which allows for more efficient, compressed storage and better performance for read-heavy analytical queries where only a subset of columns are used.
* Efficient Data Compression and Encoding: Parquet is designed to efficiently compress and encode data. Different data types can be compressed differently, which is more efficient than a one-size-fits-all approach. This results in significant storage savings and performance improvements.
* Schema Evolution: Parquet supports schema evolution. You can add new columns to your schema without needing to rewrite existing data. This makes Parquet an attractive choice for use cases where the data schema may change over time.
* Compatibility with Many Tools: Parquet is compatible with many data processing frameworks and querying tools. It's particularly popular in ecosystems that use Hadoop-based technologies, such as Hive and Impala, and it's also commonly used with Apache Spark.
* Optimized for Performance: By storing data column-wise, Parquet enables efficient read operations. For example, if a query only needs to access three columns of a table with dozens of columns, Parquet can read just those three columns, ignoring the rest of the data. This optimization significantly reduces I/O operations and speeds up data retrieval.
* Support for Nested Data Structures: Parquet can handle complex nested data structures. It can store data that is not just in traditional tabular form but also hierarchical data structures, which are common in JSON and other similar formats.
* Splitable: Parquet files can be split and processed in parallel, which is essential for distributed computing environments. This feature allows Parquet to be efficiently used in systems like Hadoop and Spark, where data needs to be processed across many nodes.
* In summary, Parquet is a powerful and efficient file format for storing and processing large-scale data. Its columnar storage design, efficient compression, and compatibility with various big data tools make it a popular choice for data warehousing and analytics tasks in a big data environment.

### Create Athena table using PARQUET files
* To create tables in Athena we will need a bucket with permissions to the user creating the table
* **Bucket Name** `ti-p-athena`
* **Folder Name** `customer-billing/parquet/`
* **File Format** `.parquet`
* **Create Table**
```sql
create external table tinitiate_athena.athena_parquet (
   order_id     int
  ,store_id     int
  ,order_date   string
  ,customer_id  int
  ,name         string
  ,email        string
  ,product_id   int
  ,quantity     int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
LOCATION 's3://ti-p-data/customer-billing/parquet';
```

### Create Athena table using Snappy compressed PARQUET files
* To create tables in Athena we will need a bucket with permissions to the user creating the table
* **Bucket Name** `ti-p-athena`
* **Folder Name** `customer-billing/parquet/`
* **File Format** `.parquet.snappy`
* **Create Table**
```sql
create external table tinitiate_athena.athena_parquet_snappy (
   order_id     int
  ,store_id     int
  ,order_date   string
  ,customer_id  int
  ,name         string
  ,email        string
  ,product_id   int
  ,quantity     int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
LOCATION 's3://ti-p-data/customer-billing/snappy-parquet';
```