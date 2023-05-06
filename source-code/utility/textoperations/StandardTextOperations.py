
def trimString(contentToTrim):

	##

	print("enter :: contentModificationTrimString()")

	##

	print("content-to-trim")
	print(contentToTrim)

	##

	print("content-to-trim // before: ")
	print(contentToTrim)

	##

	trimmedContent = contentToTrim.strip()	

	print("content-to-trim // after: ")
	print(trimmedContent)

	##

	print("returning: ")
	print(trimmedContent)

	print("exit :: contentModificationTrimString()")

	return trimmedContent

def stripString(someText):

    print("--")
    print()

    print("someText before: ["+ someText +"]")

    someText = someText.strip()

    print()
    print("someText  after: ["+ someText +"]")

    return someText

def reverseString(contentToReverse):

	##

	print("enter :: contentModificationReverseString()")

	##

	print("content-to-reverse")
	print(contentToReverse)

	##

	print("content-to-reverse // before: ")
	print(contentToReverse)

	##

	reversedContent = contentToReverse [::-1]
	reversedContent = reversedContent.strip()

	##

	print("content-to-reverse // after: ")
	print(reversedContent)

	##

	print("returning: ")
	print(reversedContent)

	print("exit :: contentModificationReverseString()")

	return reversedContent
