import boto3

# Create an SQS client
boto3.setup_default_session(profile_name='sbadmin')
sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-east-2.amazonaws.com/218058812834/sb-events-sqs-lambda-message-queue'

# Receive messages from the queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=10,
    WaitTimeSeconds=20
)
print(response)
# Get the list of messages
messages = response.get('Messages', [])
print(messages)

# Iterate through the messages and delete them
for message in messages:
    receipt_handle = message['ReceiptHandle']
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )
