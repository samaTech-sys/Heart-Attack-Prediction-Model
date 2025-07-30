# ❤️ Heart Attack Risk Prediction Model

This machine learning project predicts the **risk of a heart attack** based on patient health parameters. The goal is to assist healthcare professionals and individuals in assessing potential cardiovascular risks early using data-driven methods.

---

## 🚀 Project Overview

This end-to-end machine learning pipeline includes:

1. **Data Ingestion** – Collecting and importing the dataset.
2. **Data Validation** – Ensuring data quality and integrity.
3. **Data Processing** – Cleaning and preparing the data.
4. **Data Transformation** – Feature engineering and scaling.
5. **Data Splitting** – Separating data into training, validation, and test sets.
6. **Model Training** – Training a classifier to predict heart attack risk.
7. **Model Evaluation** – Assessing model performance with various metrics.
8. **Model Deployment** – Trained Model containerized, pushed to ECR, deployed on EC2.

---

## 🧠 Technologies Used

- Python (3.10.16)
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Jupyter Notebook
- Flask (for deployment)
- MLflow
- DVC
- GitHub Actions
- Docker
- AWS (EC2 & ECR)

---

## 📊 Features (Input Parameters)

Typical input features for this project include:

- `age`  
- `sex`  
- `total_cholesterol`  
- `ldl`  
- `hdl`  
- `systolic_bp`  
- `diastolic_bp`  
- `smoking`  
- `diabetes`  

---

## 🎯 Target Variable

The model predicts the **risk of heart attack**, represented by a binary classification:

- `0` – Low or No Risk  
- `1` – High Risk of Heart Attack

> Based on the [Heart Attack Kaggle Dataset](https://www.kaggle.com/datasets)

---

## 📁 Project Structure

```plaintext
Heart-Attack-Prediction-Model/
├── main.py
├── README.md
├── setup.py
├── requirements.txt
├── dvc.yaml
├── params.yaml
├── schema.yaml
├── heart_attack_dataset.csv
├── analysis/
│   └── EDA.ipynb
├── artifacts/
│   └── model_training/
│       └── model.joblib
├── config/
│   └── config.yaml
├── docs/
│   └── ML LifeCycle.png
├── engineering/
│   └── step1_remove_multicolinearity.ipynb
├── research/
│   └── 01_data_ingestion.ipynb → 07_model_evaluation.ipynb
├── src/
│   └── heartAttack/
│       ├── components/
│       │   ├── data_ingestion.py
│       │   ├── model_training.py
│       │   └── ...
│       ├── pipeline/
│       │   └── stage_*.py
│       ├── config/
│       ├── constants/
│       ├── entity/
│       └── utils/
└── templates/
    └── index.html
```
---
# 🛠️ Development Workflow
1. Update config.yaml
2. Update secrets.yaml (optional)
3. Update params.yaml
4. Update the entity
5. Update configuration manager in src/config
6. Update the components
7. Update the pipeline
8. Update main.py
9. Update dvc.yaml
10. Develop prediction pipeline
11. Develop app.py
12. Deploy
---

# 🚀 How to Run the Project
## STEP 1: Clone the project 
```bash 
git clone https://github.com/samaTech-sys/Heart-Attack-Prediction-Model.git
cd Heart-Attack-Prediction
```
## STEP 2: Create and Activate Conda Environment
```bash 
conda create -n heartAttack python=3.10.16
conda activate heartAttack
```
## STEP 3: Install Requirements
```bash 
pip install -r requirements.txt
```
## STEP 4: Set MLflow Credentials (for model evaluation)
```bash 
export MLFLOW_TRACKING_USERNAME=samaTech-sys
export MLFLOW_TRACKING_PASSWORD=27c279e0895284a35a6198b88076b93c13073cab
```

# 📦 DVC Commands
```bash 
dvc init      # Initializes DVC in the project
dvc repro     # Runs the DVC pipeline steps
dvc dag       # Visualizes the DVC pipeline graph
```
# 🔍 MLflow and DVC Overview
**MLflow:**
- Production-grade experiment tracking
- Logs and registers models
- Helps trace all your experiments

**DVC:**
- Lightweight, ideal for proof of concept (POC)
- Can track experiments
- Enables pipeline orchestration

# ☁️ Deployment: AWS CI/CD with GitHub Actions
## STEP 1: Login to AWS Console
## STEP 2: Create IAM User for Deployment
**Permissions Needed:**
- EC2 Access – for running virtual machines
- ECR Access – for storing Docker images

**Deployment Flow:**
- Build a Docker image from source code
- Push Docker image to ECR
- Launch an EC2 instance
- Pull Docker image from ECR to EC2
- Run Docker image on EC2

**Required IAM Policies:**
- AmazonEC2ContainerRegistryFullAccess
- AmazonEC2FullAccess

## STEP 3: Create ECR Repository
**Example:**
```bash 
805472281831.dkr.ecr.eu-north-1.amazonaws.com/cnnklassifier
```
## STEP 4: Create EC2 Ubuntu Machine
## STEP 5: Install Docker on EC2 Machine
**Optional**
```bash 
sudo apt-get update -y
sudo apt-get upgrade
```
**Required**
```bash 
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```
## STEP 6: Configure EC2 as Self-Hosted GitHub Runner
Go to GitHub → Settings > Actions > Runners → New Runner → Choose OS → Run each setup command.

## STEP 7: Setup GitHub Secrets
Set the following secrets in GitHub Actions:
env
```bash 
AWS_ACCESS_KEY_ID=your_key_id
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=eu-north-1
AWS_ECR_LOGIN_URI=https://805472281831.signin.aws.amazon.com/console
ECR_REPOSITORY_NAME=simple-app
```

# 👨‍💻 Author
Colline Tazuba (samaTech-sys)  
Open to collaborations on ML, MLOps, and data-driven problem solving.  
📧 **Email:** 2samax24@gmail.com  
📞 **Phone:** +256 789 288 903

# 📜 License
This project is licensed under the MIT License. See the LICENSE file for more information.
---