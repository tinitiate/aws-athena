# Athena tables
> Venkata Bhattaram / TINITIATE

Athena, the serverless interactive query service by AWS, empowers you to analyze massive datasets stored in S3. This guide dissects key intricacies of Athena tables, focusing on:

## Serde Formats:
* What are they? Serde (Serializer/Deserializer) defines how data is structured within a file format. It dictates how Athena interprets text-based data into usable columns.
* Supported formats: Popular choices include:
  * Parquet: Efficient columnar format with compression, ideal for large datasets.
  * ORC: Another columnar format offering good compression and fast reads.
  * CSV: Simple comma-separated format, easy to use but less efficient for larger datasets.
  * Avro: JSON-like format offering schema flexibility and data types.
* Choosing the right format: Consider factors like dataset size, access patterns, and desired performance. Athena's documentation provides detailed comparisons and guides for each format.

## Zip Formats:
* Athena supports reading data directly from ZIP archives, making it convenient to analyze compressed datasets.
* This feature helps reduce storage costs and speeds up query execution by reading compressed data without the need for prior decompression.
* Usage: Store your data in ZIP archives on Amazon S3.
* Athena can directly query the compressed data, minimizing the need for manual extraction.

## Nested Data Sets:
* Structured vs. semi-structured: Athena can handle both with appropriate configurations.
* Structured data: Use nested data types like arrays or maps within your table schema to represent hierarchical relationships.
* Semi-structured data: Leverage JSON SerDe to interpret JSON documents and access elements through dot notation.

## Array Handling:
* Arrays can be unnested, enabling you to query individual elements within the array.
* Map Handling: Athena provides functions to work with maps, allowing you to extract and manipulate key-value pairs.
* Struct Handling: Structs can be used to represent nested structures, enhancing the flexibility of your data model.