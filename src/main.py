from flask import Flask, request, render_template, jsonify
import requests
import os
from lib_version_URLPhishing.version_util import VersionUtil
from flasgger import Swagger
from prometheus_flask_exporter import PrometheusMetrics
import yaml

with open("version.yaml") as stream:
    try:
        version = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

app = Flask(__name__)
swagger = Swagger(app)
metrics = PrometheusMetrics(app)

metrics.info('app_version', 'Application version', version=version['version'])

@app.route("/", methods=["GET"])
def index():
    """
    Returns index.html to be displayed in a browser.
    """
    return render_template("index.html")


@app.route("/query", methods=["POST"])
def query():
    """
	Passes request for prediction from front end to model-service.
	---
	consumes:
  	- application/json
	parameters:
    - name: uri
      description: link to be evaluated.
      required: True
      schema:
        type: object
        required: link
        properties:
            link:
                type: string
                example: https://www.tudelft.nl/en/student/administration/termination-of-enrolment
	responses:
  	200:
    	description: "The result of the classification: 'phishing' or 'legitimate'."
	"""
    endpoint_uri = os.environ.get("MODEL_SERVICE_URI", "http://localhost:8081/")
    endpoint_uri = endpoint_uri + "predict"

    uri_to_check = request.json.get("uri")
    input_data = {
        "link": uri_to_check
    }

    response = requests.post(endpoint_uri, json=input_data)

    if response.status_code == 200:
        data = response.json()
        prediction = data.get("Prediction")
        pred_time = data.get("PredictionTime")
        model_version = data.get("ModelVersion")
        return jsonify({"Prediction": prediction,
                        "predictionTime": [pred_time],
                        "modelVersion": [model_version]})
    else:
        print("Error:", response.status_code)
        return None


@app.route("/v", methods=["GET"])
def get_version():
    """
    Returns a version from version-lib.
    ---
    responses:
      200:
        description: "Current version of the webapp."
    """
    version = VersionUtil.get_version()
    return jsonify({"version": version, "helm_name": os.environ.get("HELM_NAME", "no-name")})

metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path,
                'helm_name': os.environ.get("HELM_NAME", "no-name")}
    )
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
