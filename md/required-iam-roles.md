# IAM Roles for Athena
> Venkata Bhattaram / TINITIATE

* To use Amazon Athena, you need the appropriate AWS Identity and Access Management (IAM) roles and policies for your AWS user.

## AmazonAthenaFullAccess:
* This managed policy provides full access to Athena resources and actions.
* It includes permissions for creating and managing Athena queries, accessing query results, and working with data catalogs.
```JSON
# Example IAM policy JSON:
json
Copy code
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "athena:*",
            "Resource": "*"
        }
    ]
}
```

## AmazonS3ReadOnlyAccess:
* While Athena itself doesn't directly interact with S3 (as it's a query service), Athena queries data stored in S3 buckets. 
* Hence, you need S3 read access to enable Athena to scan and retrieve data from your S3 buckets.
* Note: Replace "your-athena-query-results-bucket" with the actual name of the S3 bucket where Athena will store query results.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::your-athena-query-results-bucket/*"
        }
    ]
}
```

## AWSGlueConsoleFullAccess (Optional):
* If you are using AWS Glue as your data catalog, this policy provides full access to the AWS Glue Console, allowing you to manage data catalogs and databases.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "glue:*",
            "Resource": "*"
        }
    ]
}
```

## Conclusion
* Ensure that these policies are attached to the IAM user, group, or role that will be interacting with Amazon Athena.
* Additionally, if you are using a data catalog like AWS Glue, make sure the IAM role associated with Athena has the necessary permissions to access and manage the Glue catalog.
* Adjust the policies based on your specific security and access requirements.
