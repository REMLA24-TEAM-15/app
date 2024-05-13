from flask import Flask, request, render_template, jsonify
import requests
import os
from lib_version_URLPhishing.version_util import VersionUtil

app = Flask(__name__)

@app.route("/", methods =["GET"])
def index ():
	return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
	endpoint_uri = os.environ.get("MODEL_SERVICE_URI", "http://localhost:8081/")
	endpoint_uri = endpoint_uri + "predict"

	uri_to_check = request.json.get("uri")
	
	params = {"link": uri_to_check}
	response = requests.post(uri_to_check, params=params)

	if response.status_code == 200:
		data = response.json()
		prediction = data.get("Prediction")
		return jsonify({"Prediction": prediction})
	else:
		print("Error:", response.status_code)
		return None

@app.route("/v", methods=["GET"])
def get_version():
	version = VersionUtil.get_version()
	return jsonify({"version": version})

app.run(host="0.0.0.0", port=8080 , debug=True)