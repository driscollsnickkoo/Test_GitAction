import boto3
import os
import json
import pymysql

conn = None

def get_connection():
    global conn
    if conn is None or not conn.open:
        conn = pymysql.connect(
            host=os.environ['DB_HOST'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASS'],
            db=os.environ['DB_NAME'],
            port=int(os.environ.get('DB_PORT', 3306)),
            connect_timeout=5
        )
    return conn

def lambda_handler(event, context):
    try:
        print("Trying to connect to:", os.environ['DB_HOST'])
        
        connection = get_connection()
        if connection:
                sns = boto3.client('sns')
                sns.publish(
                    TopicArn = 'arn:aws:sns:us-east-1:825765396866:QMPTableUpdateAlert',
                    Message = 'NK Test sns from Lambda Message',
                    Subject = 'NK TEst SNS from Lambda subject'
                )
                connection.close()
        return {
            'statusCode': 200,
            'body': json.dumps('✅ Connection to MySQL successful')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'❌ Connection failed: {str(e)}')
        }



    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('new update on git zip')             
           
    # }
