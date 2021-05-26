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
    table.update_item(Key={"group_name": event['group_name']},
    ExpressionAttributeNames={
        "#intro": "intro",
        "#master_name": "master_name",
    },
    ExpressionAttributeValues={
        ":i": event['intro'],
        ":m": event['master_name'],
    },
    UpdateExpression= "SET #intro = :i, #master_name = :m",
    )

    return {
        'statusCode': 200,
        'body': json.dumps('updated!!')
    }
