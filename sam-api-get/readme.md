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

## Getting Started
* To use this code and deploy the AWS SAM application, follow these steps:

* Install the AWS SAM CLI if you haven't already. Instructions can be found here: AWS SAM CLI Installation.

* Clone this repository to your local machine:

  ```shell
  $ git clone https://github.com/tinitiate/python-aws.git
  ```
* Navigate to the sam-api-get directory:

  ```shell
  $ cd python-aws/sam-api-get
  ```
* Build the SAM application by executing the following command:
  ```shell
  sam build
  ```

* Deploy the AWS SAM application using the SAM CLI:

  ```shell
  $ sam deploy --guided
  ```
* This command will guide you through the deployment process, prompting for configuration options.

* After the deployment is successful, the SAM CLI will provide you with the API endpoint URL. 
* You can use this URL to send GET requests to the API and receive the Json response.
