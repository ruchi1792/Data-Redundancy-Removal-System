import json
import os
import boto3

# AWS clients
dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')
sns = boto3.client('sns')

# Environment variables
TABLE_NAME = os.environ['TABLE_NAME']
BUCKET_NAME = os.environ['BUCKET_NAME']
TOPIC_ARN = os.environ['TOPIC_ARN']

# DynamoDB table
table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):
    print("Event:", event)

    # If invoked through API Gateway
    if 'body' in event:
        body = json.loads(event['body'])
    else:
        body = event

    # Get input values
    empID = body.get("empID")
    name = body.get("name")
    email = body.get("email")

    # Validate input
    if not empID or not name or not email:
        return {
            "statusCode": 400,
            "body": json.dumps("Missing Required Fields")
        }

    # Check for duplicate record
    response = table.get_item(
        Key={
            "empID": empID
        }
    )

    if 'Item' in response:
        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject="Duplicate Record",
            Message=f"Employee {empID} already exists."
        )

        return {
            "statusCode": 400,
            "body": json.dumps("Duplicate Record Found")
        }

    # Insert into DynamoDB
    table.put_item(
        Item={
            "empID": empID,
            "name": name,
            "email": email
        }
    )

    # Create JSON backup
    employee_json = json.dumps({
        "empID": empID,
        "name": name,
        "email": email
    })

    # Upload to S3
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=f"{empID}.json",
        Body=employee_json
    )

    # Send SNS notification
    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject="Employee Added",
        Message=f"Employee {empID} added successfully."
    )

    return {
        "statusCode": 200,
        "body": json.dumps("Record Added Successfully")
    }
