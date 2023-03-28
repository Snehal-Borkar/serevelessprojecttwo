import boto3    
import json
import os 

FILES_BUCKET = os.environ["FILES_BUCKET"]
def lambda_handler(event, context):   

    # create a boto3 client for S3
    s3 = boto3.client('s3')

    # specify the bucket and object key of the file you want to read
    bucket_name = FILES_BUCKET
    object_key = 'sample4.json'

    # use the S3 client to read the contents of the file
    response = s3.get_object(Bucket=bucket_name, Key=object_key)

    # extract the contents of the file
    file_content = response['Body'].read().decode('utf-8')

    # print the contents of the files
    # print(file_content)  
    return {"statusCode": 200, "body": file_content}
