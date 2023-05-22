import boto3
import json

# Creating the low level functional client
client = boto3.client('s3')
 
local_file='buckets.json'

path ='/tmp/' + local_file
bucket_name= 'pythonjun2022'
s3_file =local_file
bucketList=[]    

def lambda_handler(event, context):
    
    # Fetch the list of existing buckets
    clientResponse = client.list_buckets()
    
    # Print the buckets names 
    # print('Printing Bucket Names.....')
    
    
    for bucket in clientResponse['Buckets']:
        bucketList.append(bucket["Name"])
        # print(f'Bucket Name: {bucket["Name"]}')

    with open(path, "w") as f:
        json.dump(bucketList, f,indent=4,default=str)    
    
    try:    
        client.upload_file(path, bucket_name, s3_file)
    
        url = client.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': bucket_name,
                'Key': s3_file
            },
            ExpiresIn=24 * 10
        )

        print("Upload Successful", url)
        return url
    except FileNotFoundError:
        print("The file was not found")
        return None
    except NoCredentialsError:
        print("Credentials not available")
        return None  
    
      
    
