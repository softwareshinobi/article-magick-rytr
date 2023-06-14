
import re
from rytrme_api_python import get_text_from_rytr_me_api

LEFTDELIM="  [[[ "

MIDDLEDELIM=" // "

RIGHTDELIM=" ]]] "

def formatTextForRewrite(textToFormat):

	print(" -> :: formatTextForRewrite()")

	leftSideText = textToFormat["originalContent"]

	pattern = r'\n+'

	parts = re.split(pattern, leftSideText)
	
	thislist = []

	print()
	print("thislist:")
	print(thislist)
	print()

	print()

	for part in parts:

		part = part.strip()

		if not part:

			continue

		print(" !! " + part)

		pattern1 = r'[\!\.;\?]+'

		sentences = re.split(pattern1, part)

		print()
		print("sentences:")
		print(sentences)
		print()

		for sentence in sentences:

			if not part:

				continue

			print()
			print("sentence:")
			print(sentence)
			print()

			thislist.append(sentence.strip())

	print()

	print()
	print("rewriteCandidates:")

	print()



	fff = ""

	for rewriteCandidate in thislist:

		if not part:

			rewriteCandidate

		line = rewriteCandidate.strip()

		if line:
			
			fff = fff + (" !! "+LEFTDELIM+rewriteCandidate+MIDDLEDELIM+rewriteCandidate+RIGHTDELIM)

			fff = fff + "\n\n"

			print(LEFTDELIM+rewriteCandidate+MIDDLEDELIM+rewriteCandidate+RIGHTDELIM)

	print(" <- :: formatTextForRewrite()")

	return fff

def rewriteText(textToRewrite):

	print(" -> :: rewriteText()")
	print("    :: textToRewrite: ")

	print(textToRewrite)

	rewrittenString=""

	leftSideText = textToRewrite

	leftSideText = leftSideText.replace("\n", "")
	
	leftSideText = leftSideText.replace("[[[", "")

	print()
	print("leftSideText:")
	print(leftSideText)
	print()

	pattern = r']+'

	parts = re.split(pattern, leftSideText)

	print()
	print("parts:")
	print(parts)
	print(len(parts))
	print()

	thislist =""

	print()

	for part in parts:

		print ("Part: ",part)

		part = part.strip()

		if not part:

			continue

		if not part.startswith("!!"):

			rewrittenString = rewriteWithSpecialSauce(part)

			continue
	
	print()

	print(" <- :: rewriteText()")

	return rewrittenString

def the_secret_sauce(stringToRewrite):

	print(" -> :: rewriteWithSpecialSauce()")

	print(" <- :: rewriteWithSpecialSauce()")

	return stringToRewrite[::-1]

def rewriteWithSpecialSauce(sourceContent):

	print(" -> :: rewriteWithSpecialSauce()")

	print("Robot Rewriting Slave Reporting For Duty, Mateo")

	## building context objects

	customInputContext={'SECTION_TOPIC_LABEL': '', 'SECTION_KEYWORDS_LABEL': ''}
	customPineappleContent=sourceContent
	input_contexts={'INPUT_TEXT_LABEL': customPineappleContent}

	## call the API through the API Wrapper


## creativity_level='default' - fault | none | low | medium | high | max - change

## formats='html' - html or text - change optional
## variations = 1 - number of texts in response - change optional

	response = get_text_from_rytr_me_api(
	api_key="THZDMW3A-AWTKRM6WHMOB",
	use_case="60928476a9c7620013304e89",
	creativity_level="medium",
	formats="text",
	tone="Humorous",	
	input_contexts=input_contexts)
	
	print()
	print()

	formattedResponse = response[0].get("text")

	print()
	print("formattedResponse:")
	print(formattedResponse)
	print()

	print(" <- :: rewriteWithSpecialSauce()")

	return formattedResponse
