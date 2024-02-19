# Creating Athena Tables

## Databases and Schemas in Athena
* In Athena, databases and schemas are essentially interchangeable terms.
* They both refer to a logical namespace that groups tables together.
* Databases and schemas do not store data themselves; instead, they provide a way to organize and manage the metadata that defines the schema of your data.
* This metadata includes information about the tables in the database, such as the table name, column names, data types, and partitions.

### Creating Databases and Schemas
* Creating databases and schemas in Athena using the CREATE DATABASE statement. The statement takes the following syntax:
```sql
CREATE DATABASE tinitiate_athena
COMMENT 'Tinitiate Athena'
LOCATION 's3://ti-p-data/customer-billing';
```
* The database_name parameter is required and specifies the name of the database or schema you want to create.
* The COMMENT parameter is optional and allows you to add a comment to the database or schema.
* The LOCATION parameter is also optional and specifies the location of the data catalog where the metadata for the database or schema will be stored.

# https://medium.com/@life-is-short-so-enjoy-it/aws-athena-create-table-file-format-compression-5a90233bdbbf



## Athena CSV files
* **File Data Schema Structure**
```
order_id,store_id,order_date,customer_id,name,email,product_id,quantity
```

### Creating a table
* To create tables in Athena we will need a bucket with permissions to the user creating the table
* **Bucket Name** `ti-p-athena`
* **Folder Name** `customer-billing/csv/`
* **File Format** `CSV`
* **Create Table**
```sql
CREATE EXTERNAL TABLE tinitiate_athena.athena_csv (
   order_id     INT,
   store_id     INT,
   order_date   STRING,
   customer_id  INT,
   name         STRING,
   email        STRING,
   product_id   INT,
   quantity     INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
LOCATION 's3://ti-p-data/customer-billing/csv/'
TBLPROPERTIES ('skip.header.line.count'='1');
```

### Create Athena table using csv zip files
* To create tables in Athena we will need a bucket with permissions to the user creating the table
* **Bucket Name** `ti-p-athena`
* **Folder Name** `customer-billing/csv-gz/`
* **File Format** `CSV`
* **Create Table**
```sql
CREATE EXTERNAL TABLE tinitiate_athena.athena_csv_gz (
   order_id     INT,
   store_id     INT,
   order_date   STRING,
   customer_id  INT,
   name         STRING,
   email        STRING,
   product_id   INT,
   quantity     INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES ( 'serialization.format' = ',', 'field.delim' = ',')
LOCATION 's3://ti-p-data/customer-billing/csv/'
TBLPROPERTIES ('skip.header.line.count'='1');
```


## Athena with JSON files
* Consider the JSON data structure.
* Below we create Athena DDL table for this JSON
```json
{
  "order_id": 7169,
  "store_id": 2,
  "order_date": "2024-02-16T17:47:14",
  "customer": {
    "customer_id": 466,
    "name": "Debbie Williams",
    "email": "watsonmelissa@example.com"
  },
  "items": [
    {
      "product_id": 33,
      "product_name": "message",
      "quantity": 2,
      "price": 45.72
    },
    {
      "product_id": 54,
      "product_name": "as",
      "quantity": 1,
      "price": 25.7
    }
  ]
}
```

### Create Athena table using json files
* To create tables in Athena we will need a bucket with permissions to the user creating the table
* **Bucket Name** `ti-p-athena`
* **Folder Name** `customer-billing/json/`
* **File Format** `JSON`
* **Create Table**
```sql
create external table tinitiate_athena.athena_json (
    order_id int,
    store_id int,
    order_date string,
    customer struct<customer_id: int, name: string, email: string>,
    items array<struct<product_id: int, product_name: string, quantity: int, price: double>>
)
row format serde 'org.apache.hive.hcatalog.data.JsonSerDe'
stored as inputformat 'org.apache.hadoop.mapred.TextInputFormat'
outputformat 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
location 's3://ti-p-data/customer-billing/json/';
```

### Create Athena table using Newline delimited JSON files
* To create tables in Athena we will need a bucket with permissions to the user creating the table
* **Bucket Name** `ti-p-athena`
* **Folder Name** `customer-billing/ndjson/`
* **File Format** `JSON`
* **Create Table**
```sql
create external table tinitiate_athena.athena_ndjson (
    order_id int,
    store_id int,
    order_date string,
    customer struct<customer_id: int, name: string, email: string>,
    items array<struct<product_id: int, product_name: string, quantity: int, price: double>>
)
row format serde 'org.apache.hive.hcatalog.data.JsonSerDe'
stored as inputformat 'org.apache.hadoop.mapred.TextInputFormat'
outputformat 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
location 's3://ti-p-data/customer-billing/json/';
```


### Create Athena table using json zip files
* To create tables in Athena we will need a bucket with permissions to the user creating the table
* **Bucket Name** `ti-p-athena`
* **Folder Name** `customer-billing/gz-json/`
* **File Format** `JSON.gz`
* **Create Table**
```sql
create external table tinitiate_athena.athena_gz_json (
    order_id int,
    store_id int,
    order_date string,
    customer struct<customer_id: int, name: string, email: string>,
    items array<struct<product_id: int, product_name: string, quantity: int, price: double>>
)
row format serde 'org.apache.hive.hcatalog.data.JsonSerDe'
stored as inputformat 'org.apache.hadoop.mapred.TextInputFormat'
outputformat 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
location 's3://ti-p-data/customer-billing/gz-json/';
```

 
## Athena with PARQUET files

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