# Lambda Timestamp Demo

This simple project checks the delay between an S3 object event and a lambda invocation.

## Usage

```sh

sls deploy

# for loop to put files up to S3
for i in `seq 1 10`;
do
    aws s3 cp file.txt s3://lambda-timestamp/file$i.txt
done

sls logs -f hello 


```