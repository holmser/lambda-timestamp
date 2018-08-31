import json
import boto3
import datetime
import dateutil.parser


def lambda_handler(event, context):
    """get invocation time"""
    now = datetime.datetime.now()
    
    
    for record in event['Records']:
        """retrieve timestamp from s3 object"""
        s3_timestamp = dateutil.parser.parse(record['eventTime'])
        s3_timestamp = s3_timestamp.replace(tzinfo=None)

    payload = {
        "statusCode": 200,
        "s3TimeStamp":"{}".format(s3_timestamp),
        "lambdaTimeStamp": "{}".format(now),
        "delta": "{}".format(now-s3_timestamp),
        "body": "Success"
    }

    print(payload)
    
    return payload

