import json
import boto3

def connect():
    dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
    table = dynamodb.Table('Group')
    return table

def lambda_handler(event, context):

    try:
        table = connect()
    except Exception:
        print(Exception)
    table.delete_item(Key={'group_name': event['group_name']})
    return {
        'statusCode': 200,
        'body': json.dumps('deleted!')
    }
