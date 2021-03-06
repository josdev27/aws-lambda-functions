from __future__ import print_function
import boto3
import json
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

def lambda_handler(event, context):

    print('Initiating Function...')
    print("Received event from API Gateway: " + json.dumps(event, indent=2))
    
    # Create our DynamoDB resource using our Environment Variable for table name
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('table-name')

    try:
        response = table.query(KeyConditionExpression=Key("id").eq(event["id"]))
    except ClientError as e:
        print(e.response['Error']['Message'])
        print('Check your DynamoDB table...')
    else:
        print("GetItem succeeded:")
        print("Received response from DynamoDB: " + json.dumps(response, indent=2))
        return response["Items"][0]
