import boto3
import csv
import pandas as pd


s3_client = boto3.client('s3')
response =[]
boto3.setup_default_session(profile_name='rakeshpaluri')

s3_client = boto3.client('s3')

def lambda_handler(event, context):
	

	bucket = event['Records'][0]['s3']['bucket']['name']
	csv_file_name = event['Records'][0]['s3']['object']['key']
	csv_object = s3_client.get_object(Bucket=bucket,Key=csv_file_name)
	file_reader = csv_object['Body'].read().decode("utf-8")
	csv_data = file_reader.split("\n")
	results = list(filter(None, csv_data))
	

	for result in results:
		result_data = result.split(",")
		respone_object={}
		respone_object['id'] =result_data[0]
		respone_object['name'] =result_data[1]
		respone_object['salary'] =result_data[2]
		response.append(respone_object)
		
        
	return {'statusCode': 200,
			'body':csv(bucketList)}
	bucketList=[] 
	df = pd.DataFrame(bucketList) 
	df.to_csv('data.csv',index=False)