# AWS Lambda Python Example - `sam-img-upload` Directory

This directory contains an example AWS Lambda function implemented in Python using AWS SAM (Serverless Application Model). The function is designed to handle image file uploads to an S3 bucket.

## Prerequisites

Before you begin, make sure you have the following set up:

- AWS CLI configured with necessary credentials and region.
- AWS SAM CLI installed on your system.
- Python 3.x installed on your system.

## Folder Structure

```
sam-img-upload/
├── image_upload/
│   ├── app.py
│   ├── requirements.txt
├── template.yaml
├── README.md
```

- `image_upload`: This directory contains the Python code for the Lambda function.
  - `app.py`: Implementation of the Lambda function that handles image file uploads to an S3 bucket.
  - `requirements.txt`: List of required Python packages for the Lambda function.
- `template.yaml`: AWS SAM template defining the Lambda function, S3 bucket, and other resources.
- `README.md`: This document, providing instructions and information about using this example.

## AWS SAM Template Explanation

The `template.yaml` file is an AWS SAM (Serverless Application Model) template that defines the resources and configuration for your serverless application. Here are some key sections of the template and their explanations:

### Resources Section

This section defines the AWS resources required by your application. It specifies the resources needed to run your Lambda function and other related services:

```yaml
Resources:
  ImageUploadFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: image_upload/
      Handler: app.lambda_handler
      Runtime: python3.8
      Environment:
        Variables:
          BUCKET_NAME: !Ref ImageBucket
      Events:
        ImageUploadEvent:
          Type: S3
          Properties:
            Bucket: !Ref ImageBucket
            Events: s3:ObjectCreated:*
```

- `ImageUploadFunction`: This resource specifies the Lambda function configuration. It uses the `AWS::Serverless::Function` type.
- `CodeUri`: Specifies the relative path to the Lambda function code.
- `Handler`: Identifies the entry point function within `app.py`.
- `Runtime`: Specifies the runtime environment (Python 3.8 in this case).
- `Environment`: Sets environment variables for the function.
- `Events`: Connects the Lambda function to an S3 bucket event.

### ImageBucket Resource

This section defines the S3 bucket where the uploaded images will be stored:

```yaml
  ImageBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: my-image-bucket
```

- `ImageBucket`: This resource specifies the S3 bucket configuration.
- `BucketName`: Sets the name for the S3 bucket. You can modify this name as needed.

## AWS SAM Package Types

The `packageType` attribute in the `template.yaml` file specifies how the deployment package for the Lambda function is created. There are two package types:

- `Zip`: This is the default package type. It creates a ZIP archive of your code and dependencies. This is suitable for most use cases.
- `Image`: This package type allows you to deploy container images directly to Lambda functions. It's useful for scenarios where you want to build and deploy containerized applications.

In this example, the `ImageUploadFunction` is using the `packageType: Zip`. The `CodeUri` attribute in the function resource specifies the path to the code to be included in the ZIP package.

## `app.py` Explanation

The `app.py` file in the `image_upload` directory contains the implementation of the Lambda function that handles image file uploads to an S3 bucket. Refer to the previous section for an explanation of the code.

## Installation and Deployment

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/tinitiate/aws-lambda-python.git
   ```

2. Navigate to the `sam-img-upload` directory:

   ```
   cd aws-lambda-python/sam-img-upload
   ```

3. Build and deploy the application using AWS SAM CLI:

   ```
   sam build
   sam deploy --guided
   ```

4. Follow the prompts during deployment to configure your stack. This will include setting up the Lambda function, S3 bucket, and other resources.

## Usage

1. After deployment, AWS SAM will provide an S3 bucket to which you can upload image files.
2. You can use tools like the AWS CLI or SDKs to upload image files to the provided S3 bucket. The Lambda function will be triggered automatically upon successful uploads.

## Example Lambda Function

The Lambda function (`app.py`) in the `image_upload` directory demonstrates how to handle image file uploads to an S3 bucket. It's designed to process incoming image files, but you can extend it to perform additional tasks such as resizing images, updating a database, or triggering other AWS services.

Feel free to customize the function to match your use case and business logic.

## Notes

- This example serves as a starting point. You can modify and expand upon it to meet your application's requirements.
- Be cautious with deploying resources in your AWS account, especially if you're using this in a production environment.

## Contributing

Feel free to fork this repository and make improvements or add more examples. Pull requests are welcome!

## License

This project is licensed under the [MIT License](LICENSE).

---

This README provides detailed explanations about the structure of the example, the SAM template, package types, and the `template.yaml` file. Customize the instructions based on your specific repository structure and the complexity of your application.
