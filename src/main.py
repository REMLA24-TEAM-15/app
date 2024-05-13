from flask import Flask, request, render_template, jsonify
import requests
import os
from lib_version_URLPhishing.version_util import VersionUtil
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/", methods =["GET"])
def index ():
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
		return jsonify({"Prediction": prediction})
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
	return jsonify({"version": version})

app.run(host="0.0.0.0", port=8080 , debug=True)