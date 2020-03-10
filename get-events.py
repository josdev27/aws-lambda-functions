from __future__ import print_function
import boto3
import json
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

def lambda_handler(event, context):

    print('Initiating Function...')
    print("Received event from API Gateway: " + json.dumps(event, indent=2))
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('table-name')

    try:
        if "addedBy" in event:
            response = table.query(
                IndexName="addedBy-index",
                KeyConditionExpression=Key('addedBy').eq(event["addedBy"])
                )
        else:
            response = table.scan()
    except ClientError as e:
        print(e.response['Error']['Message'])
        print('Check your DynamoDB table...')
    else:
        print("GetItem succeeded:")
        print("Received response from DynamoDB: " + json.dumps(response, indent=2))
        return response["Items"]
