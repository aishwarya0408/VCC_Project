# Optimizing Cloud Resource Allocation for HPC Workloads

This project implements a dynamic resource provisioning framework using AWS, GCP, and Kubernetes to optimize high-performance computing (HPC) workloads.

## ⚙️ Technologies Used

- AWS Auto Scaling
- Google Cloud Functions
- Kubernetes (GKE/EKS)
- Terraform
- Prometheus & CloudWatch

## 📂 Project Structure

- `infrastructure/` – Terraform scripts to provision cloud infrastructure
- `src/` – Scripts to deploy and manage workloads
- `monitoring/` – Configurations for Prometheus and CloudWatch
- `architecture/` – System architecture diagram

## 🚀 Getting Started

### Prerequisites

- Terraform
- AWS CLI & GCP SDK
- kubectl

### Deployment

```bash
# Initialize Terraform
cd infrastructure
terraform init

# Apply Infrastructure
terraform apply
