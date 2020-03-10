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
        response = table.update_item(
            Key={"id": event["id"]},
            ExpressionAttributeNames={
                "#addedBy": "addedBy",
                "#date": "date",
                "#description": "description",
                "#title": "title",
                "#location": "location"
            },
            ExpressionAttributeValues= {
                ":addedBy":event["addedBy"],
                ":date":event["date"],
                ":description":event["description"],
                ":title":event["title"],
                ":location":event["location"]
            },
            UpdateExpression =  ("SET #addedBy = :addedBy,"  
                                "#date = :date,"  
                                "#description = :description," 
                                "#title = :title," 
                                "#location = :location")
            )
    except ClientError as e:
        print(e.response['Error']['Message'])
        print('Check your DynamoDB table...')
    else:
        print("UpdateItem succeeded:")
        print("Received response from DynamoDB: " + json.dumps(response, indent=2))
        return event
