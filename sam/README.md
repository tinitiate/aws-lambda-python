# AWS SAM
* This repository contains code for a Python application that uses AWS Serverless Application Model (SAM) to create a Lambda Function and ivoke the Function locally.
* The code is organized as follows:
  ```shell
  sam/
  ├── README.md
  ├── template.yaml  
  └── get-s3-buckets/
      ├── app.py
      ├── requirements.txt    

  ```
 `README.md`
 * This is the readme file you are currently reading. It provides an overview and instructions for using the code in this repository.
  
 `get-s3-buckets/`
 * This directory contains the code for the AWS SAM application.

 `app.py`
 * This is the main Python file that defines the Lambda function logic. 

  `requirements.txt`
  * This file lists the Python dependencies required by the application. 
  * It includes the boto3 library, which is used to connect with `aws`.

 `template.yaml`
  * This file is the AWS SAM template file that describes the AWS resources needed for deploying the application.
  *  It defines the Lambda function, and other necessary resources.
