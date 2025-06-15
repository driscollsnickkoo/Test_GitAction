import boto3
import json

def lambda_handler(event, context):
    sns = boto3.client('sns')
    sns.publish(
        TopicArn = 'arn:aws:sns:us-east-1:825765396866:QMPTableUpdateAlert',
        Message = 'NK Test sns from Lambda Message',
        Subject = 'NK TEst SNS from Lambda subject'
    )

    
    return {
        'statusCode': 200,
        'body': json.dumps('new update on git zip')             
           
    }
