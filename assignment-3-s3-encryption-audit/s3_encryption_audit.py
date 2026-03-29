import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    buckets = s3.list_buckets()

    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']
        try:
            s3.get_bucket_encryption(Bucket=bucket_name)
            print(f"{bucket_name}: Encryption enabled")
        except Exception:
            print(f"{bucket_name}: Encryption NOT enabled")
