# Creating Athena Tables with JSON files
* JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate. It is based on a subset of the JavaScript Programming Language, but its use has expanded beyond JavaScript to become one of the primary formats for data interchange on the web and in other applications. Here are some key aspects of JSON:
* Text-based and Language-independent: JSON is a text format that is completely language-independent but uses conventions familiar to programmers of the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. This property makes JSON an ideal data-interchange language.
* Structure: JSON is built on two structures:
* A collection of name/value pairs. In various languages, this is realized as an object, record, struct, dictionary, hash table, keyed list, or associative array.
An ordered list of values. In most languages, this is realized as an array, vector, list, or sequence.
* Data Types: JSON supports various data types - strings, numbers, booleans (true/false), arrays (ordered sequences of values), and objects (collections of key/value pairs). It does not support binary data directly, but binary data can be encoded in strings and included in JSON.
* Human Readable and Writeable: The concise syntax and structure of JSON make it easily readable and understandable by humans, facilitating data interchange between people and systems.
* Widely Used for APIs and Configurations: JSON is extensively used in web APIs and configuration files. It provides a simple way to store and communicate structured data over a network and between different components of an application.
* Flexibility: JSON does not require a predefined schema, and data can be nested in a hierarchical structure. This makes JSON flexible but also means that applications consuming JSON must handle variations in the structure.
* Parsing and Serialization: JSON data can be easily parsed and serialized (converted to and from strings) by most programming languages, making it a convenient format for storing and transmitting data.
* Efficiency and Performance: While not as efficient as binary formats in terms of size and speed, JSON strikes a good balance between performance and accessibility, making it suitable for many applications where data interchange is crucial.
* In summary, JSON is a ubiquitous, text-based data format that emphasizes simplicity, readability, and language independence. Its widespread adoption in web APIs, configuration files, and many other areas makes it a cornerstone of modern data interchange.
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

## Create Athena table using json files
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

## Create Athena table using Newline delimited JSON files
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

## Create Athena table using json zip files
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
