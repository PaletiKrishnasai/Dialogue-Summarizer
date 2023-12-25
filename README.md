# Dialogue-Summarizer

This project focuses on the end-to-end implementation of dialogue summarization using the PEGASUS transformer model finetuned on samsum dataset.

# Workflow

These are the steps that should be followed while implementing each step in the project like data ingestion, data validation, data transformation, model training and model evaluation.

- Step 1: Update config.yaml
- Step 2: Update params.yaml
- Step 3: Update entity
- Step 4: Update the Configuration Manager in src config
- Step 5: Update the components
- Step 6: Update the pipeline
- Step 7: Update main.py
- Step 8: Update app.py

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

    #with specific access

    1. EC2 access : It is virtual machine

    2. ECR: Elastic Container registry to save your docker image in aws


    #Description: About the deployment

    1. Build docker image of the source code

    2. Push your docker image to ECR

    3. Launch Your EC2

    4. Pull Your image from ECR in EC2

    5. Lauch your docker image in EC2

    #Policy:

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image

    - Save the URI:

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:

    #optinal

    sudo apt-get update -y

    sudo apt-get upgrade

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

# 6. Configure EC2 as self-hosted runner:

    setting>actions>runner>new self hosted runner> choose os> then run command one by one

# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY= (downed secret key from AWS account)

    AWS_REGION = us-east-2 (this will vary depending on your AWS account region)

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app

# 8. HuggingFace:

The HuggingFace Folder contains the files required to push to HuggingFace Hub and deploy the model card Spaces.

    Dialogue_Summarizer_notebook : Contains the complete codebase to train, finetune and push to hub.

    HuggingFaceSpacesApp: Contains the complete Application code to host on HuggingFace Spaces. (Just rename the file to app.py while hosting)

    requirements.txt : Contains the requirements for the hugging face application. (Upload the file to spaces folder).

**Model card:** https://huggingface.co/pk248/pegasus-samsum

# 9. Corresponding Images:

![Github Actions Deployement](/images/GithubActions_2.png)
_CI-CD pipeline through Github Actions_

![Github Actions Deployement completed](/images/GithubActions.png)
_CI-CD pipeline through Github Actions_

![AWS Hosted Application using FastAPI](/images/AWS_hosted.png)
_AWS Hosted Application using FastAPI_

![HuggingFace Hosted Application using Streamlit](/images/HuggingFaceSpacesDemoApp.png)
_HuggingFace Hosted Application using Streamlit_
