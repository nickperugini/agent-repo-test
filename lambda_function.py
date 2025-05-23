
import boto3
import os
from datetime import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = os.environ['BUCKET_NAME']
    filename = f"upload-{datetime.utcnow().isoformat()}.txt"
    content = "This is a test upload from Lambda."

    s3.put_object(Bucket=bucket_name, Key=filename, Body=content)

    return {
        'statusCode': 200,
        'body': f'File {filename} uploaded to {bucket_name}'
    }
