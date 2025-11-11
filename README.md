# 🏗️ AWS 3-Tier Flask Application

A scalable 3-tier web application deployed on AWS using Terraform and Docker.

## 📋 Overview

This project deploys a Flask application on AWS with a 3-tier architecture:
- **Web Tier**: EC2 instances with Nginx (Public Subnet)
- **Application Tier**: Flask application in Docker (Private Subnet)
- **Database Tier**: Amazon RDS MySQL/PostgreSQL (Private Subnet)

## 🛠️ Tech Stack

- **Cloud**: AWS (EC2, RDS, VPC, ALB)
- **IaC**: Terraform
- **Application**: Flask (Python)
- **Containerization**: Docker
- **Web Server**: Nginx


## 🚀 Deployment Steps

### 1. Clone the Repository
```bash
git clone https://github.com/omdivekar14/Aws-3tier-project.git
cd Aws-3tier-project
```

### 2. Configure AWS Credentials
```bash
aws configure
```

### 4. Deploy Infrastructure
```bash
cd terraform
terraform init
terraform plan
terraform apply -auto-approve
```

## 📸 Screenshots

### Terraform Apply Success
<img width="1244" height="353" alt="Screenshot 2025-11-11 120551" src="https://github.com/user-attachments/assets/363cc13c-74b2-48d7-aa0f-7a11b669faea" />

*Infrastructure successfully deployed using Terraform*

### EC2 Instances Running
<img width="1665" height="306" alt="Screenshot 2025-11-11 142003" src="https://github.com/user-attachments/assets/91615412-d512-4060-b36b-7b87ff542bcd" />

*EC2 instances running in web and application tiers*

### Flask Application
<img width="1009" height="256" alt="Screenshot 2025-11-11 133203" src="https://github.com/user-attachments/assets/d9a842c0-7d89-40db-a336-b9978cb67404" />

*Flask application accessible through browser*
### VPC Network ACLs
<img width="1911" height="761" alt="Screenshot 2025-11-11 141114" src="https://github.com/user-attachments/assets/87b3a83d-ad32-460a-a429-9162cf734d00" />

### RDS Database
<img width="1919" height="772" alt="Screenshot 2025-11-11 141214" src="https://github.com/user-attachments/assets/a081b6f7-d66f-41e3-8a78-0cf3a4911e34" />

*RDS database successfully deployed*

## 🗑️ Cleanup

To delete all resources:
```bash
terraform destroy -auto-approve
```

## 👤 Author

**Om Divekar**
- GitHub: [@omdivekar14](https://github.com/omdivekar14) 
