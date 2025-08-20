# AWS Learning Plan for Enterprise-Level Cloud Deployment

## Objective
To learn and implement enterprise-level cloud deployment concepts using AWS Free Tier, focusing on hosting, scalability, deployment, containerization, backup, and system design concepts. By the end of this plan, you will have a strong understanding of AWS features and enterprise-level cloud practices.

## Prerequisites
1. AWS Free Tier account created after July 15, 2025.
2. Basic understanding of Python and Flask.
3. GitHub account for version control.
4. AWS CLI installed and configured locally.
5. Docker installed locally.

---

## Day-by-Day Plan

### **Day 1: Setting Up the Environment**
- **Objective**: Prepare the local and cloud environment for deployment.
- **Tasks**:
  1. Install and configure AWS CLI.
  2. Set up an IAM user with programmatic access and attach the `AdministratorAccess` policy.
  3. Configure AWS CLI with the IAM user credentials.
  4. Push the current project to a GitHub repository.
  5. Learn about AWS Free Tier limits and services.

### **Day 2: Hosting the Application on EC2**
- **Objective**: Deploy the Flask app on an EC2 instance.
- **Tasks**:
  1. Launch an EC2 instance (t2.micro) with Amazon Linux 2.
  2. SSH into the instance and install Python, Flask, and required dependencies.
  3. Transfer the application code to the EC2 instance.
  4. Run the Flask app and access it via the public IP.
  5. Learn about security groups and configure them to allow HTTP traffic.

### **Day 3: Automating Deployment with Elastic Beanstalk**
- **Objective**: Use Elastic Beanstalk for managed deployment.
- **Tasks**:
  1. Install the Elastic Beanstalk CLI.
  2. Initialize an Elastic Beanstalk application.
  3. Deploy the Flask app using Elastic Beanstalk.
  4. Learn about Elastic Beanstalk environments and scaling options.

### **Day 4: Containerization with Docker**
- **Objective**: Containerize the application using Docker.
- **Tasks**:
  1. Write a Dockerfile for the Flask app.
  2. Build and test the Docker image locally.
  3. Push the Docker image to Amazon Elastic Container Registry (ECR).
  4. Deploy the containerized app on an EC2 instance.

### **Day 5: Scaling with Load Balancers and Auto Scaling**
- **Objective**: Implement scalability using AWS services.
- **Tasks**:
  1. Set up an Application Load Balancer (ALB).
  2. Configure Auto Scaling Groups (ASG) for the EC2 instances.
  3. Test the scalability by simulating traffic.

### **Day 6: Database Integration**
- **Objective**: Add a managed database to the application.
- **Tasks**:
  1. Launch an RDS instance (MySQL or PostgreSQL).
  2. Connect the Flask app to the RDS database.
  3. Test CRUD operations with the database.

### **Day 7: Backup and Disaster Recovery**
- **Objective**: Learn about backup and recovery strategies.
- **Tasks**:
  1. Set up automated backups for the RDS instance.
  2. Learn about S3 and store application logs and backups.
  3. Test recovery by restoring a backup.

### **Day 8: Monitoring and Logging**
- **Objective**: Monitor the application and infrastructure.
- **Tasks**:
  1. Set up CloudWatch for monitoring metrics and logs.
  2. Create alarms for critical metrics (e.g., CPU usage, memory).
  3. Learn about AWS X-Ray for tracing requests.

### **Day 9: CI/CD Pipeline**
- **Objective**: Automate deployments using a CI/CD pipeline.
- **Tasks**:
  1. Set up a CodePipeline for the application.
  2. Integrate GitHub as the source for the pipeline.
  3. Automate testing and deployment to Elastic Beanstalk.

### **Day 10: Final Review and Optimization**
- **Objective**: Review and optimize the deployment.
- **Tasks**:
  1. Review the architecture and identify bottlenecks.
  2. Optimize costs by analyzing AWS usage.
  3. Document the entire process and lessons learned.

---

## Deliverables
1. Flask app deployed on AWS with enterprise-level features.
2. GitHub repository with daily commits and documentation.
3. Comprehensive understanding of AWS services and system design concepts.

---

## Notes
- Focus on learning while implementing.
- Utilize AWS Free Tier limits effectively.
- Document each step and push changes to GitHub daily.
