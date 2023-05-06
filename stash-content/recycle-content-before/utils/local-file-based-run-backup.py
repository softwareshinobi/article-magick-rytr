from rytrme_api_python import get_text_from_rytr_me_api

def split_string_on_periods(string_to_split):

    parts = string_to_split.split(".")
    
    print("parts: ")
    print(parts)

    for part in parts:

        part = part.strip()

        print()

        print("------------------------------")
        print("")
        print("applying operation to string: ")
        print("")
        print(part)
        print("")
        print("------------------------------")

        print()

        if not part:

            print ("bad string. skipping.")

            continue

   
        print(part)
        print()

        operatedString = part.strip()




        if part:

            operatedString = stir_the_secret_sauce(part)

        print()
        print("operatedString: ")
        print()
        print(operatedString)
        print()

        print("------------------------------")
        print("sending content to file")
        print("------------------------------")
   
        save_rewritten_content_to_file(operatedString)

def stir_the_secret_sauce(sourceContent):

    print()
    print("Secret Sauce Reporting For Duty")


    print()
    print("Input String:")
    print(sourceContent)
    print()

  #  print()
  #  print("Stirring The Sauce.")
  #  print()

    ## The Secret Sauce
    rewrittenContent = the_secret_sauce(sourceContent)

    #rewrittenContent = rewrittenContent.strip()

    print()
    print("rewritten String:")
    print(rewrittenContent)
    print()

   ## print("returning: ", rewrittenContent)
   ## print("exit :: stir_the_secret_sauce()")

    return rewrittenContent

def the_secret_sauce2(sourceContent):

    return sourceContent

def the_secret_sauce(sourceContent):

    print("Robot Rewriting Slave Reporting For Duty, Mateo")

    ## building context objects

    customInputContext={'SECTION_TOPIC_LABEL': '', 'SECTION_KEYWORDS_LABEL': ''}
    customPineappleContent=sourceContent
    input_contexts={'INPUT_TEXT_LABEL': customPineappleContent}

    ## call the API through the API Wrapper
    response = get_text_from_rytr_me_api(
    api_key="ETUOP79VGWWDLRCF1YQE9",
    use_case="60928476a9c7620013304e89",
    creativity_level="max",
    formats="text",
    input_contexts=input_contexts)
    tone="Humorous"

    print()
    print()

 #   print("raw response")
 #   print(response)

  #  print()
 #   print()

  #  for x in range(len(response)):
      #  print()
     #   print(response[x].get("text"))
       # print()

    formattedResponse = response[0].get("text")
    
    return formattedResponse

def save_rewritten_content_to_file(fname):

    print ("f name")
    print (fname)

    f = open('content-area/output-content/special-seo-content-fairy-article.md', "a")
    
    f.write(fname)
    f.write(".")

    f.write("\n")
    f.write("\n")

    f.close()

def cleanString(someText):

    print("--")
    print()

    print("someText before: ["+ someText +"]")

    someText = someText.strip()

    print()
    print("someText  after: ["+ someText +"]")

    return someText

def doRewriteAndClean(someText):

    print("--")
    print()

    print("someText before: ["+ someText +"]")

    someText = someText [::-1]

    someText = someText.strip()

    print()
    print("someText  after: ["+ someText +"]")

    return someText


with open('content-area/input-content/some-article-for-inspiration-purposes.md') as f:

    lines = f.readlines()

   # print("hello?")

   # print(lines)

    for line in lines:

        print()
        print("current line:")
        print()
        print(line)
        print()

        # x = i.replace(".", ".\n\n")
      #  x = x.strip();
        #  print(x)

        sample = split_string_on_periods(line)

        # print("sample")
        #print(sample)

     #   save_rewritten_content_to_file(sample)


