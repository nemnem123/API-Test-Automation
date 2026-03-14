# API Test Automation with CI/CD

## Architecture
API Gateway → Lambda → DynamoDB

## Automation Test
Tests are written using pytest.

## CI/CD Pipeline
GitHub Actions performs:

1. Install Python
2. Install dependencies
3. Run pytest
4. Deploy Lambda if tests pass

## Run locally

pytest -v