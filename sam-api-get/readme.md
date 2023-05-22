# This repository contains code for a Python application that uses AWS Serverless Application Model (SAM) to create a simple API endpoint that handles GET requests.
```shell
sam-api-get/
  ├── api-get.py
  ├── requirements.txt
  └── template.yaml

```
`sam-api-get/`
* This directory contains the code for the AWS SAM application to take inputs from API Gateway and return the JSON.
`api-get.py`
* This is the main Python file that defines the API endpoint logic. 
* In this example, it returns the details of the customers from loans schema as JSON.

`requirements.txt`
* This file lists the Python dependencies required by the application. 
* It includes the aws-psycopg2 library, which is used to retrieve the data from Postgres Database.

`template.yaml`
* This file is the AWS SAM template file that describes the AWS resources needed for deploying the application.
* It defines the API Gateway, Lambda function, and other necessary resources.
