# AWS Lambda Python Example - `sam-api-post`
---
This directory contains an example AWS Lambda function implemented in Python using AWS SAM (Serverless Application Model). The function is designed to handle HTTP POST requests.

## Prerequisites

Before you begin, make sure you have the following set up:

- AWS CLI configured with necessary credentials and region.
- AWS SAM CLI installed on your system.
- Python 3.x installed on your system.

## Folder Structure

```
sam-api-post/
├── sam-api-post/
│   ├── postgres-insert.py
│   ├── requirements.txt
├── template.yaml
├── README.md
```

- `sam-api-post`: Contains the Python code for the Lambda function.
  - `postgres-insert.py`: Implementation of the Lambda function.
  - `requirements.txt`: List of required Python packages.
- `template.yaml`: AWS SAM template defining the Lambda function, API Gateway, and other resources.
- `README.md`: This document, providing instructions and information about using this example.

## AWS SAM Template Explanation

The `template.yaml` file is an AWS SAM (Serverless Application Model) template that defines the resources and configuration for your serverless application. Here are some key sections of the template and their explanations:

### Resources Section

This section defines the AWS resources required by your application. It specifies the resources needed to run your Lambda function and other related services:

```yaml
Resources:
  GetProductFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: sam-api-post/
      Handler: postgres-insert.handler
      Runtime: python3.8
      Events:
        HelloWorldApi:
          Type: Api
          Properties:
            Path: /get-product
            Method: POST
```

- `GetProductFunction`: This resource specifies the Lambda function configuration. It uses the `AWS::Serverless::Function` type.
- `CodeUri`: Specifies the relative path to the Lambda function code.
- `Handler`: Identifies the entry point function within `postgres-insert.py`.
- `Runtime`: Specifies the runtime environment (Python 3.8 in this case).
- `Events`: Connects the Lambda function to an API Gateway event.

### Environment Variables

The `Environment` variables can be set in the Lambda function configuration. In this example, environment variables are used to store database connection details:

```yaml
      Environment:
        Variables:
          DATABASE_HOST: mydatabase.xxxxxx.us-east-1.rds.amazonaws.com
          DATABASE_PORT: "5432"
          DATABASE_NAME: mydatabase
          DATABASE_USER: myuser
          DATABASE_PASSWORD: mypassword
```

These variables are accessed within the `postgres-insert.py` code to establish a connection to the PostgreSQL database.

## `postgres-insert.py` Explanation

The `postgres-insert.py` file in the `sam-api-post` directory contains the implementation of the Lambda function that handles HTTP POST requests. Refer to the previous section for an explanation of the code.

## Installation and Deployment

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/tinitiate/aws-lambda-python.git
   ```

2. Navigate to the `sam-api-post` directory:

   ```bash
   cd aws-lambda-python/sam-api-post
   ```

3. Build the application using AWS SAM CLI:

   ```bash
   sam build
   ```

4. Local Invocation and Testing:

   Test the Lambda function locally using the AWS SAM CLI. Run the following command from the root directory of the `sam-api-post` example:

   ```bash
   sam local invoke GetProductFunction --event events/event.json
   ```

   Replace `events/event.json` with the path to your event data file.

5. Local API Testing:

   Start a local API Gateway to test the Lambda function using the following command:

   ```bash
   sam local start-api
   ```

   This will provide you with local endpoints that you can use to send HTTP requests.

6. Deployment:

   Deploy the application using AWS SAM CLI:

   ```bash
   sam deploy --guided
   ```

   Follow the prompts during deployment to configure your stack. This will include setting up the Lambda function, API Gateway, and other resources.

## Usage

1. After deployment, the API Gateway endpoint URL will be provided. Use this URL to send HTTP POST requests to trigger the Lambda function.

## Lambda Function

The Lambda function (`postgres-insert.py`) in the `sam-api-post` directory demonstrates handling HTTP POST requests and interacting with a PostgreSQL database. The function can be further customized to suit your specific use case.

---

This README provides detailed explanations about the structure of the example, the SAM template, the `postgres-insert.py` code, instructions for local testing and deployment, and explanations for the environment variables. Customize the instructions based on your specific repository structure and the complexity of your application.
