from __future__ import print_function
import boto3
import json
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
import uuid

def lambda_handler(event, context):

    print('Initiating Function...')
    print("Received event from API Gateway: " + json.dumps(event, indent=2))
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('table-name')
    try:
        event["id"] = str(uuid.uuid4())
        response = table.put_item(
            Item=event)
    except ClientError as e:
        print(e.response['Error']['Message'])
        print('Check your DynamoDB table...')
    else:
        print("Create User succeeded:")
        print("Received response from DynamoDB: " + json.dumps(response, indent=2))
        return event
