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

---

## 🧠 Technologies Used

- Python (3.8+)
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Jupyter Notebook
- (Optional) Streamlit/Flask for deployment

---

## 📊 Features (Input Parameters)

Typical input features may include:
- Age
- Sex
- Chest pain type
- Resting blood pressure
- Cholesterol level
- Fasting blood sugar
- Maximum heart rate achieved
- Exercise-induced angina
- ST depression induced by exercise
- Number of major vessels
- Thalassemia type

> These features are based on the [Heart Disease UCI Dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease) or a similar dataset.

---

## 📁 Project Structure

```plaintext
heart-attack-risk-prediction/
│
├── data/                  # Raw and processed datasets
├── notebooks/             # Jupyter notebooks for exploration & modeling
├── src/                   # Source code modules
│   ├── ingestion.py
│   ├── validation.py
│   ├── processing.py
│   ├── training.py
│   ├── evaluation.py
│   └── utils.py
│
├── models/                # Saved models
├── outputs/               # Reports, metrics, plots
├── app/                   # (Optional) Web app files
│
├── README.md
├── requirements.txt
└── main.py

----
## 🛠️ Development Workflow 
1. Update config.yaml
2. Update secrets.yaml [optional]
3. Update params.yaml
4. Update the entity
5. Update configurations manager in src config 
6. Update the components 
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. Develop prediction pipeline
11. Develop app.py
12. Deploy 

# How to run the project?
### STEPS
Clone the project 

... bash 
https://github.com/samaTech-sys/Rising-Village-Prediction-Model.git
...

### STEP 01 Create a conda environemnt after opening the repository 
... bash 
conda create -n heartAttack python=3.10.16
...

... bash 
conda activate heartAttack
...

### STEP 02 Install the requirements
... bash 
pip install -r requirements.txt
...

### STEP 03 Credentials for connect to mlflow (during model evalation) 

... bash 
export MLFLOW_TRACKING_USERNAME=samaTech-sys
export MLFLOW_TRACKING_PASSWORD=27c279e0895284a35a6198b88076b93c13073cab

...

### DCV Commands

1. dvc init (initilaises dvc in my project)
2. dvc repro (duns the dvc steps)
3. dvc dag (Visualises the dvc pipeline)

## About MLflow and DVC 
MLflow 
    - Its production Grade 
    - Trace all your expriments 
    - Logging and targing your model 

DVC 
    - Its very light weight for POC only 
    - lite weight experiments tracker
    - It can perform orchestration(Creating pipelines)

# -------------Deployment---------------------- #

# AWS-CICD-Deployment-with-Gihub-actions

## 1. Login into AWS Console 

## 2. Create IAM user for deployment 
   #with specific access
   1. EC2 access: It is a virtual machine 
   2. ECR: Elastic container reistry to save your docker image

    #Decsription: about the deployment 
    1. Build a docker image of the source code 
    2. Push your docker image to ECR 
    3. Launch your ECR 
    4. Push your image from ECR to EC2
    5. Launch your docker image in EC2

    #Policy: 
    1. AmazonEC2ContainerRegistryFullAccess
    2. AmazonEC2FullAccess

## 3. Create EC2 Repo to store/save docker image 
    - save the url: 805472281831.dkr.ecr.eu-north-1.amazonaws.com/cnnklassifier
    
## 4. Creete EC2 Ubuntu Machine 

## 5. Open EC2 and install docker in EC2 Machine 
    #optional 
    sudo apt-get update -y 
    sudo apt-get upgrade 

    #required 
    sudo sh get-docker.sh 

    sudo usermod -aG docker ubuntu 

    newgrp docker 

## 6. Configure EC2 as self-hosted runner:
Open your github account: setting>actions>runner>new self>choose os> then run command one by one 

## 7. Set up github access 
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION = eu-north-1
AWS_ECR_LOGIN_URI= demo>>> https://805472281831.signin.aws.amazon.com/console
ECR_REPOSITORY_NAME=simple-app
