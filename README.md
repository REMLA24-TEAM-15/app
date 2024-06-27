# App Service
This is the flask app that users interact with as a part of the URL phishing detection project. \
[GitHub Pages](https://remla24-team-15.github.io/app/) 

It is recommended to run the application using docker-compose. More instructions are present in the [Operation](https://github.com/REMLA24-TEAM-15/Operation) repository.

![img](https://github.com/REMLA24-TEAM-15/Operation/blob/deployments/Documentation/AppFrontEnd.png)

## Setup Instructions
To set up locally , make sure [model-service](https://github.com/REMLA24-TEAM-15/model-service) is up and running locally.

### Prerequisites
 * Python 3.10 is required to run the code.
 * Create a conda environment :

   ```conda create --name remlapy310 python=3.10 ```

   ``` conda activate remlapy310 ```

 * To install the required packages , we use [poetry](https://python-poetry.org/docs/). To install and run poetry , use the following commands.

   ```pip install poetry ```

1. Install dependencies with poetry:
```bash
poetry install --no-root
```
2. Run the app (on port 8080)
```bash
$ python src/main.py
```
Open any URLs in the terminal to make a prediction!

## Prometheus Metrics
1. 'by_path_counter': This metric counts the number of prediction requests received by the app.
2. 'spam/not_spam' : This metric counts the number of spam and not_spam predictions made by the app. 



## Tokens Required:
For this repository you require a GitHub token (e.g GH_Token) with package and repo read/write permissions. 
