import boto3    
import json
import os  
def lambda_handler(event, context):    

    # extract the contents of the file
    content = {
        "name":"Snehal",
        "location": "Chandrapur",
        "Organisation": "Konf",
        "Designation": "SDE"
    }


    # print the contents of the files
    # print(file_content)  
    return {"statusCode": 200, "body": json.dumps(content)}
