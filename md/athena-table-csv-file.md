# Creating Athena Tables
* CSV (Comma-Separated Values) is a simple, widely used file format for storing tabular data. It is used in a variety of domains, such as data export/import in spreadsheets and databases, data processing in scientific applications, and for data interchange between systems. The format is straightforward and has several key characteristics:
* Simple Structure: A CSV file is essentially a text file containing data that is separated by commas (or sometimes other delimiters like semicolons or tabs). Each line in the file corresponds to a row in the table, and each comma-separated value corresponds to a cell.
* Ease of Use: CSV files can be easily created, edited, and viewed using a simple text editor. They are also supported by most spreadsheet applications (like Microsoft Excel or Google Sheets) and can be imported into or exported from many databases and data processing tools.
* Wide Compatibility: Due to its simplicity and text-based nature, CSV is a highly compatible format that can be used across different programs, applications, and operating systems.
* Lack of Standardization: While the basic concept of CSV is straightforward, there is no strict standardization, which can lead to compatibility issues. For example, the way text is enclosed, special characters are handled, and line breaks are implemented can vary.
* No Type Information: CSV does not store type information for its data. All data is stored as plain text, which means that the consuming application needs to interpret the data correctly, often based on context or predefined knowledge about the data structure.
* Not Suitable for Hierarchical Data: CSV is ideal for flat data structures (simple lists or tables) but is not suitable for hierarchical or complex data structures. It lacks the ability to handle multi-dimensional data natively.
* Efficiency: While CSV files are more efficient in size compared to some formats like XML or JSON, they do not support compression natively. For very large datasets, this might lead to inefficiencies in storage and speed.
* Use in Data Exchange and ETL Processes: CSV is commonly used in data exchange processes between different systems and in ETL (Extract, Transform, Load) processes because of its ease of handling and wide support.
* In summary, CSV is a simple, widely adopted format for storing and exchanging tabular data. Its simplicity and wide compatibility make it a popular choice for many applications, particularly where the data structure is flat and uncomplicated. However, the lack of standardization and type information can sometimes be a limitation for more complex data handling needs.

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
