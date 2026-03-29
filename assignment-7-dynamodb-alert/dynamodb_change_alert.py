import json
import boto3

sns = boto3.client('sns')

SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:338295026911:DynamoDBChangeAlerts"

def lambda_handler(event, context):
    for record in event['Records']:
        event_name = record['eventName']

        message = {
            "EventType": event_name,
            "Keys": record['dynamodb'].get('Keys', {}),
            "OldImage": record['dynamodb'].get('OldImage', {}),
            "NewImage": record['dynamodb'].get('NewImage', {})
        }

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=f"DynamoDB {event_name} Alert",
            Message=json.dumps(message, indent=2, default=str)
        )

    return {"statusCode": 200}
