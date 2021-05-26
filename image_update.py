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
    table.update_item(
    Key={"group_name": event['group_name']},
    ExpressionAttributeNames={
        "#group_pic": "group_pic",
    },
    ExpressionAttributeValues={
        ":p": "https://imagehackerton.s3.ap-northeast-2.amazonaws.com/imagehackerton/" + event['group_pic'] + ".jpg",
    },
    UpdateExpression="SET #group_pic = :p",
)
    