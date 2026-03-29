import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client('s3')

BUCKET_NAME = 'assignment2-s3-cleanup-rohan-vijay-mangate'
DAYS_OLD = 30

def lambda_handler(event, context):
    deleted_files = []
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    if 'Contents' in response:
        for obj in response['Contents']:
            age = datetime.now(timezone.utc) - obj['LastModified']
            if age > timedelta(days=DAYS_OLD):
                s3.delete_object(Bucket=BUCKET_NAME, Key=obj['Key'])
                deleted_files.append(obj['Key'])

    print("Deleted files:", deleted_files)
    return {"statusCode": 200, "deleted": deleted_files}
