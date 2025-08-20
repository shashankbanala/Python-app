# Day 1 Progress

## Objective
Prepare the local and cloud environment for deployment.

---

## Steps Performed

### 1. Installed and Configured AWS CLI
- Downloaded and installed AWS CLI.
- Verified installation using:
  ```powershell
  aws --version
  ```

### 2. Set Up IAM User
- Logged into AWS Management Console.
- Created a new IAM user with programmatic access.
- Attached `AdministratorAccess` policy to the user.
- Downloaded access key and secret key.

From terminal:
 ```powershell
  aws configure
  ```
- Configured AWS CLI with credentials:
  - Access Key ID
  - Secret Access Key
  - Default region: `us-east-1`
  - Default output format: `json`


### 3. Reviewed AWS Free Tier
- Explored AWS Free Tier limits and services from [AWS Free Tier Page](https://aws.amazon.com/free/).
- Focused on services like EC2, S3, RDS, Elastic Beanstalk, and CloudWatch.

---

## Deliverables
- AWS CLI installed and configured.
- IAM user created with programmatic access.
- Project pushed to GitHub.
- Familiarity with AWS Free Tier limits.

---

## Notes
- All steps were successfully completed.
- Ready to proceed to Day 2 tasks.
