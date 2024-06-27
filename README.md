# App Service
This is the flask app that users interact with as a part of the URL phishing detection project.

## Setup Instructions




## Release in a docker image

1. **Build docker image:**
   ```bash
   sudo docker build -t flaskapp .

2. **Run docker conatiner on port 8080:**
   ```bash
   sudo docker run -p8080:8080 flaskapp

## Run locally

1. Install dependencies with poetry:
   ```bash
   poetry install --no-root

2. Run (on port 8080):
   ```bash
   python3 src/main.py