# AWS SAM - AWS Lambda to Fetch S3 Buckets
* This repository contains code for a Python application that leverages the AWS Serverless Application Model (SAM) to define, deploy, and test a Lambda Function which lists the names of all S3 buckets.
* Directory Structure
  ```shell
  sam/
  ├── README.md                 - This documentation.
  ├── template.yaml             - SAM template for defining AWS resources.
  └── get-s3-buckets/
      ├── app.py                - The main Lambda function.
      └── requirements.txt      - Python dependencies required by the application.


  ```
 `README.md`
 * This is the readme file you are currently reading. It provides an overview and instructions for using the code in this repository.
  
 `get-s3-buckets/`
 * This directory contains the code for the AWS SAM application.

 `app.py`
 * This Python script contains the main logic of the Lambda function. The function:

    * Initializes a low-level S3 client using boto3.
    * Fetches a list of existing S3 buckets.
    * Prints and collects the bucket names.
    * Returns the bucket names in the response.

  `requirements.txt`
  * This file lists the Python dependencies required by the application. 
  * It includes the boto3 library, which is used to connect with `aws`.

 `template.yaml`
  * Defines the AWS resources required by the application. The main components include:
    
    * GetS3BucketsFunction: This defines the Lambda function properties like name, description, code location, handler, runtime, timeout, etc.
    * Events: Defines the API Gateway trigger for the Lambda function. In this case, the path /buckets with the method get is used to trigger the Lambda.
