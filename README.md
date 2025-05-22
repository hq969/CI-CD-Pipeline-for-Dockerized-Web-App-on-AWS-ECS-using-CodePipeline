# 🚀 AWS CI/CD Deployment – Flask App on ECS with CodePipeline

This project demonstrates how to build and deploy a **Dockerized Flask web application** to **Amazon ECS (Fargate)** using a fully automated **CI/CD pipeline** built with **AWS CodePipeline**, **CodeBuild**, and **CodeDeploy**.

---

## 🔧 Tech Stack

- **Language**: Python 3.11 (Flask 3.0)
- **Containerization**: Docker
- **Infrastructure**:
  - Amazon ECS (Fargate)
  - Amazon ECR (Elastic Container Registry)
  - AWS CodePipeline (CI/CD Orchestration)
  - AWS CodeBuild (Image Build & Push)
  - AWS CodeDeploy (Blue/Green ECS Deployment)
  - Amazon S3 (Artifacts)
  - GitHub / CodeCommit (Source Repo)

---

## 📁 Project Structure

myapp/

├── app.py

├── Dockerfile

├── requirements.txt

├── buildspec.yml

└── imagedefinitions.json 



---

## 🚦 CI/CD Pipeline Flow

1. **Code Commit**:
   - Code is pushed to GitHub or AWS CodeCommit.
2. **CodePipeline Trigger**:
   - Pipeline is automatically triggered.
3. **CodeBuild Phase**:
   - Builds Docker image from Dockerfile.
   - Tags and pushes image to ECR.
   - Generates `imagedefinitions.json` file.
4. **CodeDeploy Phase**:
   - ECS Service is updated with new image (zero-downtime Blue/Green).
5. ✅ **Deployed Flask App** is now live on ECS Fargate!

---

## 📦 Requirements

- AWS CLI Configured
- IAM Roles:
  - CodePipelineRole
  - CodeBuildRole
  - ECS TaskExecutionRole
- Amazon ECS Cluster & Service created with:
  - Launch type: Fargate
  - Container name: `myapp-container`
- Amazon ECR Repo created (`myapp`)
- S3 Bucket for artifacts (optional but recommended)

---

## 🔍 Key Files

### `app.py`
A simple web app using Flask 3.0:

```python
@app.route("/")
def index():
    return "✅ Deployed Flask 3.0 App via AWS ECS + CodePipeline 🚀"




---


## 🧪 Testing the App
After successful deployment, access your application via:

Application Load Balancer (ALB) DNS name

OR ECS Task public IP (if configured)

✅ Deployed Flask 3.0 App via AWS ECS + CodePipeline 🚀


## 📈 Optional Enhancements
Add unit tests to CodeBuild phase

Add CloudWatch Logs for ECS service

Configure Blue/Green Deployment with health checks

Setup GitHub Actions instead of CodeBuild for CI

Add Slack or Email Notification using SNS


## 📄 License
MIT License – free to use and modify.


## 👨‍💻 Author
Harsh Sonkar
AWS | Python | DevOps | Full Stack | Data Engineer



