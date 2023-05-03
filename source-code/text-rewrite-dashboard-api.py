#!/usr/bin/env python

import json

from utility utility-text-manipulation the_secret_sauce

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=["GET"])
def returnHeadddlthCheckMessageGET():
	return "The Content rewriting api appears to be up now"

@app.route('/', methods=["POST"])
def returnHeadddlthCheckMessagePOST():
	return "The Content rewriting api appears to be up now (POST)"

@app.route('/health-check', methods=["GET"])
def returnHealthCheckMessageGET():
	return ":: CONTENT REWRITER API IS UP ::"

@app.route('/health-check', methods=["POST"])
def returnHealthCheckMessagePOST():
	return ":: CONTENT REWRITER API IS UP :: (POST)"


@app.route('/content/rewrite-content', methods=["GET"])
def contentRewriterGET():

	print("enter -- contentRewriterGET")

	##	jsonData = json.loads(request.data)

	jsonData = request.data

	print("request data: ");
	print (jsonData);

	print("json request data: ")
	print(jsonData )

	##contentToRewrite = json.loads(request.data)['content']

	contentToRewrite = request.data['content']

	print("content to rewrite: ")
	print(contentToRewrite)

	rewrittenContent = the_secret_sauce(contentToRewrite)

	print("rewrittenContent : ")
	print(rewrittenContent )

	print("exit  -- contentRewriterPOST")

	return rewrittenContent 

@app.route('/content/rewrite-content', methods=["POST"])
def contentRewriterPOST():

	print("enter -- contentRewriterPOST22")

	#jsonData = json.loads(request.data)

	jsonData = request.data

	print("json request data: ")
	print(jsonData )

##	contentToRewrite = json.loads(request.data)['content']

	contentToRewrite =request.data

	print("content to rewrite: ")
	print(contentToRewrite)

	rewrittenContent = the_secret_sauce(contentToRewrite)

	print("rewrittenContent : ")
	print(rewrittenContent )

	print("exit  -- contentRewriterPOST22")

	return rewrittenContent 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
