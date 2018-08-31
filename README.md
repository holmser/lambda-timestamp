# Lambda Timestamp Demo

This simple project checks the delay between an S3 object event and a lambda invocation.

## Usage

```

sls deploy

aws s3 cp file.txt s3://your-bucket-name/

sls logs -f hello 

```