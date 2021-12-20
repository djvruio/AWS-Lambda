# What It Does?
This is a repository of various Lambdas functions that I have written. They do various tasks such as CRUD operations in Dynamo, fetch images from S3, post event to Amazon EventBridge, check EC2 tags, etc. Please let me know if you have a question on a specific program.

# Things I Learned
- AWS Lambda
- What defines serverless:
    - No servers to provision or manage.
    - Automatically scales with usage (Up and Down).
    - Never pay for idle (Pay only for what you use).
    - Avalilability and fault-tolerance built-in.
    - No AMI rehydration.
- Python coding.
- Boto 3 (AWS SDK for Python).
- Event driven patterns.
- Cloud9

# How To Run?
- Create a Lambda Function from AWS console with Python as the language.
- Create the appropriate IAM role.
- Once Lambda Function is created, copy and paste the code from the Python programs into your Lambda code
- Save the Lambda Function.
- Configure a test event if necessary.
- Run the Lambda Function.