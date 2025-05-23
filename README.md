# AWS Lambda + API Gateway + S3 (Terraform)

This Terraform project provisions a simple AWS architecture with:

-  **Lambda Function** that uploads a file to S3
-  **API Gateway (HTTP API)** that triggers the Lambda
-  **S3 Bucket** to store uploaded files

Each time the API endpoint is invoked, the Lambda uploads a timestamped text file to the S3 bucket.

---

##  Architecture Diagram

[Client] --> [API Gateway] --> [Lambda Function] --> [S3 Bucket]

yaml

.
├── main.tf # Core resources: Lambda, API Gateway, S3
├── outputs.tf # API Gateway endpoint output
├── variables.tf # (Empty, for future use)
├── lambda_function.py # Lambda function logic
├── lambda_function_payload.zip # Zipped Lambda code
