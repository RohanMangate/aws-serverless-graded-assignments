import boto3
from datetime import datetime, timezone

s3 = boto3.client('s3')

BUCKET_NAME = "rohan-s3-log-cleaner"
RETENTION_DAYS = 90

def lambda_handler(event, context):
    deleted_files = []
    now = datetime.now(timezone.utc)

    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    if 'Contents' in response:
        for obj in response['Contents']:
            age_days = (now - obj['LastModified']).days
            if age_days > RETENTION_DAYS:
                s3.delete_object(Bucket=BUCKET_NAME, Key=obj['Key'])
                deleted_files.append(obj['Key'])

    print("Deleted log files:", deleted_files)
    return {"statusCode": 200}
