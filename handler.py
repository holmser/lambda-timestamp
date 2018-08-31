import json
import boto3
import botocore
import datetime
import dateutil.parser


def lambda_handler(event, context):
    """get invocation time"""
    now = datetime.datetime.now()
    s3 = boto3.resource('s3')


    
    for record in event['Records']:
        """retrieve timestamp from s3 object"""
        s3_timestamp = dateutil.parser.parse(record['eventTime'])
        s3_timestamp = s3_timestamp.replace(tzinfo=None)

        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        try:
            s3.Bucket(bucket).download_file(key, '/tmp/file.txt')
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise

        


    payload = {
        "statusCode": 200,
        "object": "{}/{}".format(bucket, key),
        "s3TimeStamp":"{}".format(s3_timestamp),
        "lambdaTimeStamp": "{}".format(now),
        "delta": "{}".format(now-s3_timestamp),
        "body": "Success"
    }

    print(payload)
    
    return payload

