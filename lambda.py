import json
import os
import random
import boto3

s3 = boto3.client('s3')
sns = boto3.client('sns')

BUCKET = os.environ['BUCKET_NAME']
KEY = os.environ['OBJECT_KEY']
TOPIC_ARN = os.environ['SNS_TOPIC_ARN']

def lambda_handler(event, context):
    # 1) Read quotes.json from S3
    try:
        response = s3.get_object(Bucket=BUCKET, Key=KEY)
        content = response['Body'].read().decode('utf-8')
        data = json.loads(content)
    except Exception as e:
        return {"error": f"Unable to read S3 file: {str(e)}"}

    quotes = data.get("quotes", [])
    if not quotes:
        return {"error": "Quotes file is empty or missing 'quotes' key."}

    # 2) Pick a random quote
    quote = random.choice(quotes)

    # 3) Send via SNS
    try:
        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject="Daily Motivation",
            Message=quote
        )
    except Exception as e:
        return {"error": f"Unable to send SNS message: {str(e)}"}

    return {
        "status": "success",
        "sent_quote": quote
    }
