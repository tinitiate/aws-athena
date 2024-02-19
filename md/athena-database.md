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
