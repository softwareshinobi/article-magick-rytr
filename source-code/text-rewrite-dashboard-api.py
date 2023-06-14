#!/usr/bin/env python

###

import json

from flask import Flask, request, jsonify

from flask_cors import CORS, cross_origin

##

from utility.textoperations.RytrTextOperations import formatTextForRewrite, rewriteText

##

app = Flask(__name__)

###

cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

###

@app.route('/', methods=["GET"])
@cross_origin()
def handleRootRequestGET():

	statusMessage = "hello from / *GET*"

	print(statusMessage)

	return statusMessage

@app.route('/health-check', methods=["GET"])
@cross_origin()
def handleHealthCheckGET():

	statusMessage = "standard text API Is Up! [flask]"

	print(statusMessage)

	return statusMessage

@app.route('/', methods=["POST"])
@cross_origin()
def handleRootRequestPOST():

	statusMessage = "hello from / *POST*"

	print(statusMessage)

	return statusMessage

###

@app.route('/text-operations/format-text', methods=["POST"])
@cross_origin()
def handlePOSTFormatText():

	contentToFormat = request.get_json()

	print("content to format: ")
	print(contentToFormat)

	statusMessage = formatTextForRewrite(contentToFormat)

	print(statusMessage)

	return statusMessage

###

@app.route('/text-operations/rewrite-text', methods=["POST"])
@cross_origin()
def handlePOSTRewriteText():

	contentToRewrite = request.get_json()

	#print("content to rewrite: ")
	#print(contentToRewrite)

	statusMessage = rewriteText(contentToRewrite)

	#print(statusMessage)

	return statusMessage

###

@app.after_request
def handle_options(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, X-Requested-With"

    return response

def main():

	print()
	print("###")

	print("### This is the Text Rewrite Dashboard API")
	
	print("###")
	print()

if __name__ == "__main__":
    
	#main()
    
	app.run(host='0.0.0.0', port=44444, debug=True)
