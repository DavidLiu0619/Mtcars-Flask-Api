# Mtcars Flask API – Homework 3  
**Course**: STATS 418  
**Student**: Hengyuan (David) Liu  

This project builds and serves a simple linear regression model through a Flask API using the classic `mtcars.csv` dataset. The model predicts the **miles per gallon (mpg)** of a car based on six numerical predictors.

The project is fully containerized using Docker and deployed to **Google Cloud Run**. Anyone should be able to clone this repo, follow the setup steps, and reproduce the deployment.

---

## Repository Structure

| File | Description |
|------|-------------|
| `mtcars.csv` | Dataset used for model training |
| `mtcars.ipynb` | Jupyter notebook for model training, feature selection, and evaluation |
| `prediction.py` | Python script containing the prediction function |
| `server.py` | Flask application that serves the API |
| `Dockerfile` | Instructions to build the Docker image |
| `docker-compose.yml` | Used to launch the app locally via Docker |
| `requirements.txt` | List of Python dependencies |
| `curl_test.sh` | Test Commend Lines

---

## Model Features

The model uses the following features to predict `mpg`:

- `wt` – Vehicle weight  
- `am` – Transmission (0 = automatic, 1 = manual)  
- `qsec` – 1/4 mile time  
- `gear` – Number of forward gears  
- `drat` – Rear axle ratio  
- `cyl` – Number of cylinders  

---

## Local Testing with Docker

### 1. Clone this repository:
```bash
git clone <your-repo-url>
cd Mtcars-Flask-Api
```

### 2. Build and run the app locally:
```bash
docker compose up -d
```

### 3. Test the API:
Verify the server is running:
```bash
curl http://localhost:5050/
```
**Expected output**:
```
Server is up - Mtcars Flask API running!
```

Test a prediction:
```bash
curl -H "Content-Type: application/json" \
     -X POST \
     -d '{"wt":3.73,"am":1,"qsec":17.6,"gear":4,"drat":3.07,"cyl":8}' \
     http://localhost:5050/predict_mpg
```
**Expected output**:
```json
{"predicted mpg": 18.4314781529401}
```

---

* You can change some of the values to see the prediction change. 
* Both of the curl commands can be found in the file curl_test.sh.
* Check to see if you have any docker containers running using
  ```bash
  docker container ls
  ```
* stop them through
    ```bash
    docker componse down -v
     ```

## Deployment on Google Cloud Run

If deployed, you can test the live API using this command:

```bash
curl -X POST \
     "https://mtcars-flask-app-980752141572.us-central1.run.app/predict_mpg" \
     -H "Content-Type: application/json" \
     -d '{"wt":3.73,"am":1,"qsec":17.6,"gear":4,"drat":3.07,"cyl":8}'
```

**Expected output**:
```json
{"predicted mpg": 18.4314781529401}
```

> If the API is not available, you can rebuild and deploy it by:
> - Building your Docker image  
> - Pushing to Docker Hub  
> - Deploying to Google Cloud Run using your own project

---
