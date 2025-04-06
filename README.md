# Blue-Green Deployment Demo with AWS App Runner

This is a simple Flask application that demonstrates blue-green deployment patterns using AWS App Runner and GitHub Actions.

## Project Overview

This demo showcases:
- Blue-green deployment strategy
- CI/CD pipeline with GitHub Actions
- Security scanning for secrets and vulnerabilities
- Automated testing
- Containerization with Docker
- Deployment to AWS App Runner

## How it Works

The application visually changes based on which deployment version is active:
- **Blue version**: Light blue background
- **Green version**: Light green background

## Branches

- `main`: Main development branch
- `blue`: Blue deployment branch
- `green`: Green deployment branch

## Security Features

This project includes several security checks:
- Secret detection with `detect-secrets`
- Code security scanning with `bandit`
- Dependency vulnerability scanning with `safety`
- Code linting with `flake8`

## Deployment Process

1. Push changes to either the `blue` or `green` branch
2. GitHub Actions workflow runs:
   - Security scans
   - Tests
   - Builds Docker image
   - Pushes to ECR
   - Deploys to AWS App Runner

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
export APP_VERSION=blue  # or 'green'
python app.py

# Run tests
pytest
```

## AWS App Runner Setup

The application is deployed to AWS App Runner, which manages the containerized application and handles the blue-green deployment switching.

## CI/CD Pipeline

The GitHub Actions workflow in `.github/workflows/ci-cd.yml` handles:
1. Security scanning
2. Testing
3. Building Docker image
4. Deploying to AWS App Runner

## Blue-Green Deployment Strategy

To perform a blue-green deployment:
1. Make changes to the non-active branch (`blue` or `green`)
2. Push changes and let CI/CD deploy the new version
3. Test the new version
4. Switch traffic by updating the App Runner service configuration

## Required GitHub Secrets

- `AWS_ACCESS_KEY_ID`: AWS access key
- `AWS_SECRET_ACCESS_KEY`: AWS secret key
- `AWS_ACCOUNT_ID`: Your AWS account ID