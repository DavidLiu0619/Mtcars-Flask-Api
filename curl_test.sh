#!/bin/bash

curl http://localhost:5050/

# Test the Flask app running on localhost:5050
curl -H "Content-Type: application/json" -X POST -d '{"wt":3.73,"am":1,"qsec":17.6,"gear":4,"drat":3.07,"cyl":8}' "http://localhost:5050/predict_mpg"

# Test the Flask app running on Google Cloud Run
curl -X POST "https://mtcars-flask-app-980752141572.us-central1.run.app/predict_mpg" -H "Content-Type: application/json" -d '{"wt":3.73,"am":1,"qsec":17.6,"gear":4,"drat":3.07,"cyl":8}'
