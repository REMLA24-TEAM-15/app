from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

@app.route('/', methods =['GET'])
def index ():
	return render_template('index.html')

@app.route("/query", methods=["POST"])
def query():
	data = True
	if data:
		return jsonify({"success": True})
	else:
		return jsonify({"success": False})

app.run(host="0.0.0.0", port =8080 , debug=True)