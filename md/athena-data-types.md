# Athena Data Types

* Athena is based on the Apache Hive data definition language (DDL) so the data 
  types are similar to those used in Hive. 

* **Numeric Types**:
  * tinyint: 8-bit signed integer.
  * smallint: 16-bit signed integer.
  * int or integer: 32-bit signed integer.
  * bigint: 64-bit signed integer.
  * float: Single-precision 32-bit floating-point number.
  * double: Double-precision 64-bit floating-point number.
  * decimal: Arbitrary-precision decimal numbers.
* **String Types**:
  * varchar or char: Variable-length or fixed-length character strings.
  * string: Synonym for varchar.
  * char: Fixed-length character strings.
* **Temporal Types**:
  * date: Represents a date in the format 'YYYY-MM-DD'.
  * time: Represents a time in the format 'HH:MM:SS'.
  * timestamp: Represents a timestamp in the format 'YYYY-MM-DD HH:MM:SS'.
  * interval: Represents a duration or time span.
* **Boolean Type**:
  * boolean: Represents a boolean value (true or false).
* **Binary Types**:
  * binary: Represents binary data.
* **Complex Types**:
  * array: Represents an ordered collection of elements.
  * map: Represents an unordered collection of key-value pairs.
  * struct or row: Represents a structure or record.
* **Other Types**:
  * row: Represents a structure or record (similar to struct).
  * any: Represents any valid data type.


## Struct and Array
* Consider the below JSON
```json
{
  "invoice_id": 1,
  "invoice_date": "11/29/2011 11:15:05",
  "store_id": 3,
  "customer_invoice_details": [
    {
      "invoice_detail_id": 1,
      "product_id": 8,
      "quantity": 8
    },
    {
      "invoice_detail_id": 2,
      "product_id": 2,
      "quantity": 5
    }
  ]
}
```
* Table DDL for the above JSON
```sql
CREATE EXTERNAL TABLE invoices (
  invoice_id INT,
  invoice_date timestamp,
  store_id INT,
  customer_invoice_details ARRAY<STRUCT<invoice_detail_id: INT, product_id: INT, quantity: INT>>
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES ('ignore.malformed.json' = 'true')
LOCATION 's3://your-s3-bucket/your-data-path/';
```

* Insert for the above JSON
```sql
INSERT INTO invoices VALUES (
  1,
  '11/29/2011 11:15:05',
  3,
  ARRAY(
    STRUCT(1, 8, 8),
    STRUCT(2, 2, 5),
    STRUCT(3, 25, 2)
  )
);
```
