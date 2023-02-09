# GitHub-Actions Continuous Deployment (CD)
### [Part 2 of the project of the week from DataTalksClub](https://github.com/DataTalksClub/project-of-the-week/blob/main/2023-02-08-github_actions-2.md)

Continuous Deployment is a software development practice where code changes are automatically built, tested, and deployed to production. It allows teams to release changes quickly and with confidence, improving the speed and efficiency of the development process.

Continuous Deployment using GitHub Actions involves the following steps:

- Create a new workflow file in your GitHub repository's .github/workflows directory. The workflow file should specify the steps that need to be taken for Continuous Deployment.
- Configure the steps in your workflow to build, test, and deploy your code. This may involve setting up environment variables, checking out your code, and running scripts.
- Push your code changes to your GitHub repository to trigger the workflow.
- Monitor the progress of your workflow from the Actions tab in your GitHub repository.
- Optionally, you can set up notifications for successful or failed deployments by using the GitHub Actions API and webhooks.



# fastapi-car-price-pred

This repository contains an example of a API that serves a ML model using FastAPI. It was created as part of [Project of the Week at DataTalks.Club](https://github.com/DataTalksClub/project-of-the-week).

The goal of this project is to predict the prices of Ford cars. It uses the [Ford Car Price Prediction](https://www.kaggle.com/datasets/adhurimquku/ford-car-price-prediction) dataset.


## Running the API

You can run this project either locally or using Docker.

### Running the API locally

Before running the API locally, make sure you have [Conda installed](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

To run this project locally, you need to follow these steps:

1. Create a new conda environment:
   
   ```
   conda create --name fastapi-car-price-pred
   ```

2. Activate the conda environment:

   ```
   conda activate fastapi-car-price-pred
   ```

3. Install the project dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run the API:
   
   ```
   python main.py
   ```


### Running the API using Docker

Before running the API with Docker, make sure that you install it following these [steps](https://docs.docker.com/get-docker/).

To run the API using Docker:

1. Build the Docker image:

   ```
   docker build -t fastapi-car-price-pred . 
   ```

2. Run the API:

   ```
   docker run -p 8000:8000 fastapi-car-price-pred
   ```