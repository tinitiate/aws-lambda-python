import boto3

boto3.setup_default_session(profile_name='sbadmin')

client = boto3.resource('sqs')
queue = client.get_queue_by_name(QueueName='sb-events-sqs-lambda-message-dlq-queue')

response = queue.send_message(MessageBody='error from Python Lambda!')

print(response)