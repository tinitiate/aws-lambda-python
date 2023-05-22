import boto3
import json

# Creating the low level functional client
client = boto3.client('s3')

def s3buckets(event, context):
    
    # Fetch the list of existing buckets
    clientResponse = client.list_buckets()
    
    # Print the buckets names 
    print('Printing Bucket Names.....')
    bucketList=[]    
    
    for bucket in clientResponse['Buckets']:
        bucketList.append(bucket["Name"])
        print(f'Bucket Name: {bucket["Name"]}')

    return {
        "statusCode": 200,
        "body": json.dumps(bucketList)
    }