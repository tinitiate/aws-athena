# Creating Athena Tables

## Databases and Schemas in Athena
* In Athena, databases and schemas are essentially interchangeable terms.
* They both refer to a logical namespace that groups tables together.
* Databases and schemas do not store data themselves; instead, they provide a way to organize and manage the metadata that defines the schema of your data.
* This metadata includes information about the tables in the database, such as the table name, column names, data types, and partitions.

### Creating Databases and Schemas
* Creating databases and schemas in Athena using the CREATE DATABASE statement. The statement takes the following syntax:
```sql
CREATE DATABASE mydatabase
COMMENT 'My sample database'
LOCATION 's3://my-bucket/glue-catalog'
```
* The database_name parameter is required and specifies the name of the database or schema you want to create.
* The COMMENT parameter is optional and allows you to add a comment to the database or schema.
* The LOCATION parameter is also optional and specifies the location of the data catalog where the metadata for the database or schema will be stored.

# https://medium.com/@life-is-short-so-enjoy-it/aws-athena-create-table-file-format-compression-5a90233bdbbf


## Create Athena table using csv files
### Creating a table
* To create tables in Athena we will need a bucket with permissions to the user creating the table
* **Bucket Name** `ti-p-athena`
* **Folder Name** ``
* **File Format** ``
* **File Data Schema Structure**
```
```
* **Create Table**
```sql
```
### Adding data to the athena table folder


## Create Athena table using csv zip files
* To create tables in Athena we will need a bucket with permissions to the user creating the table
* **Bucket Name** `ti-p-athena`
* **Folder Name** ``
* **File Format** ``
* **Data Schema Structure**
```
```
* **Create Table**
```sql
```
