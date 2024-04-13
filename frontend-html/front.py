from flask import Flask, request, jsonify,render_template,redirect, jsonify, Response
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)
here=""
@app.route('/')
def form():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
@app.route('/login/', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/registration')
@app.route('/registration/')
def registration():
    return render_template('registration.html')

@app.route("/addrec", methods=['GET','POST'])
@app.route("/addrec/", methods=['GET','POST'])
def addrec():
	if request.method == 'POST':
		here=request.form
		response = requests.post('http://localhost:5000/registration',json=dict(here))

	if response.status_code == 200:
		return render_template('thanks.html')
	else:
		return Response(response.content, response.status_code)

@app.route("/chkrec", methods=['GET','POST'])
@app.route("/chkrec/", methods=['GET','POST'])
def chkrec():
	if request.method == 'POST':
		here=request.form
		response = requests.post('http://localhost:5000/login',json=dict(here))

	if response.status_code == 200:
		response_dict = json.loads(response.text)
		result = response_dict["result"]
		if result == "true":
			return render_template('success.html')
		else:
			return render_template('fail.html')
	else:
		return Response(response.content, response.status_code)

if __name__ == "__main__":
    app.run(debug= False,port=5001,host="0.0.0.0")
