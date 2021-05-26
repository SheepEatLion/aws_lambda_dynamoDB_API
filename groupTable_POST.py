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
    #url = boto3.client('s3').generate_presigned_url(
    #ClientMethod='get_object', 
    #Params={'Bucket': 'imagehackerton', 'Key': 'default_picture'},
    #ExpiresIn=3600)
    table.put_item(Item={'group_name':event['group_name'],
        'master_name':event['master_name'],
        'open_date':event['open_date'],
        'meeting_date': "",
        'meeting_type': "",
        'meeting_intro': "",
        'intro':event['intro'],
        'participant':[event['master_name']],
        'group_pic': 'https://imagehackerton.s3.ap-northeast-2.amazonaws.com/imagehackerton/'+ event['group_name']+'.jpg',
        'dona': "0",
        'dona_all': "0",
        'loc': event['loc'],
    })
    return {
        'statusCode': 200,
        'body': json.dumps('inserted!')
    }
