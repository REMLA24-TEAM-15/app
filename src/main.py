from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods =['GET'])
def index ():
	return render_template('index.html')

@app.route("/query", methods=["POST"])
def query():
	uri = request.json.get("uri")
	url = "http://model-service:8081/predict"
	params = {"URI": uri}
	response = requests.post(url, params=params)

	if response.status_code == 200:
		data = response.json()
		is_phishing = data.get("is_phishing")
		return jsonify({"is_phishing": is_phishing})
	else:
		print("Error:", response.status_code)
		return None

@app.route("/v", methods=["GET"])
def get_version():
	return jsonify({"version": "-1.0.0"})

app.run(host="0.0.0.0", port=8080 , debug=True)