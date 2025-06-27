# Flask CI/CD Deployment

This repository contains a Flask application integrated with a fully automated CI/CD pipeline and Kubernetes deployment.

---

## Project Features

* Flask-based microservice
* Docker containerization
* GitHub Actions CI/CD pipeline
* Kubernetes deployment on AWS EKS
* Health checks and monitoring
* Logging and observability
* Secure practices with RBAC, Secrets, and NetworkPolicies

---

## Local Development Setup

### Prerequisites

* Python 3.11
* Docker

### Steps

```bash
git clone https://github.com/<your-username>/flask-cicd-app.git
cd flask-cicd-app
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app/main.py
```

Access app at: `http://localhost:5000/health`

---

## CI/CD Pipeline Setup

### Trigger

* The pipeline is triggered on every push to the `main` branch.

### CI/CD Includes:

* Linting with flake8
* Unit testing with pytest
* Docker image build and push to Docker Hub
* Health check inside a container
* Deployment to AWS EKS

### 🐳 Docker Build & Run

```bash
docker build -t flask-cicd-app .
docker run -d -p 5000:5000 flask-cicd-app
```

---

### GitHub Secrets Required

| Secret Name             | Description                     |
| ----------------------- | ------------------------------- |
| `DOCKERHUB_USERNAME`    | Docker Hub username             |
| `DOCKERHUB_TOKEN`       | Docker Hub access token         |
| `AWS_ACCESS_KEY_ID`     | AWS access key                  |
| `AWS_SECRET_ACCESS_KEY` | AWS secret access key           |
| `AWS_REGION`            | AWS region (e.g., `ap-south-1`) |
| `EKS_CLUSTER_NAME`      | Name of your EKS cluster        |

---

## Kubernetes Deployment

### Prerequisites

* AWS CLI configured
* `kubectl` installed
* EKS cluster created and configured

### Steps

```bash
# Configure kubeconfig
aws eks update-kubeconfig --region <region> --name <cluster-name>

# Apply manifests
kubectl apply -f k8s/

# Get LoadBalancer URL
kubectl get svc flask-service
```

Visit the `EXTERNAL-IP` shown in browser: `http://<elb-endpoint>`

---

## Monitoring & Observability

Detailed documentation is available in [monitoring.md](./monitoring.md)

Includes:

* Prometheus + Flask Exporter
* Health probes and alerting rules
* Centralized logging options with Fluent Bit, Loki, etc.

YAML examples for:

* `prometheus-config.yaml`
* `cloudwatch-logs-config.yaml`
* `RBAC.yaml`
* `network-policy.yaml`

---

## Security & Best Practices

See full details in [security.md](./security.md)

Highlights:

* Use of private image repositories
* Image vulnerability scanning
* Least-privilege IAM and RBAC
* Secrets handling via GitHub & Kubernetes
* Auto-rollbacks and resource limits
* Network policy enforcement

---

## Assumptions

* Kubernetes cluster (EKS) is pre-created
* GitHub secrets are correctly configured
* Docker Hub is used for image hosting
* A `ConfigMap` named `flask-config` exists with key `APP_ENV`

---

## Summary

This project demonstrates end-to-end DevOps practices:

* CI/CD automation via GitHub Actions
* Secure Docker image builds with health checks
* Kubernetes deployment with monitoring and logging
* Clear separation of configuration and secrets
