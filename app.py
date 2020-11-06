from flask import Flask, request, make_response
import json
import os
from flask_cors import cross_origin
from SendEmail.sendEmail import EmailSender
#from logger import logger
from email_templates import template_reader

app = Flask(__name__)


"""
{
  "responseId": "b84733b6-7ca2-4c86-a794-40aea39779fa-ee7586fb",
  "queryResult": {
    "queryText": "what is speech",
    "parameters": {
      "Question": "what is speech",
      "email": "dushantkumar172@gmail.com"
    },
    "allRequiredParamsPresent": true,
    "fulfillmentMessages": [
      {
        "text": {
          "text": [
            ""
          ]
        }
      }
    ],
    "intent": {
      "name": "projects/fee-related-vichxd/agent/intents/704ab63d-8087-4280-868f-9f0a51eb1f07",
      "displayName": "QA"
    },
    "intentDetectionConfidence": 0.3,
    "languageCode": "en"
  },
  "outputAudio": "UklGRiQAAABXQVZFZm10IBAAAAABAAEA//////7///8CABAAZGF0YQAAAAA=",
  "outputAudioConfig": {
    "audioEncoding": "OUTPUT_AUDIO_ENCODING_LINEAR_16",
    "synthesizeSpeechConfig": {
      "speakingRate": 1,
      "voice": {
        "name": "en-US-Wavenet-G"
      }
    }
  },
  "agentId": "314344be-1b14-4077-b01b-de02986bc7cd",
  "agentSettings": {
    "enableAgentWideTts": true
  }
}
"""
#r= json.load(request)
#print(r)
# geting and sending response to dialogflow
@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():

    req = request.get_json(silent=True, force=True)

    #print("Request:")
    #print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    #print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


# processing the request from dialogflow
def processRequest(req):
    #log = logger.Log()

    sessionID=req.get('responseId')


    result = req.get("queryResult")
    user_says=result.get("queryText") #question
    #log.write_log(sessionID, "User Says: "+user_says)
    parameters = result.get("parameters")
    ques = parameters.get("Question")
    email = parameters.get("email")


    Q_A = result.get("intent").get('displayName')
    if ( Q_A=='QA'):

        email_sender=EmailSender()
        template= template_reader.TemplateReader()
        email_message=template.read_course_template(Q_A)
        email_sender.send_email_to_student(email,email_message)
        email_file_support = open("email_templates/support_team_Template.html", "r")
        email_message_support = email_file_support.read()
        email_sender.send_email_to_support(cust_email=email,ques=ques,body=email_message_support)
        fulfillmentText="An email has been sent to the a relavant person with your asked question and contact information, you'll be contacted soon."
        #log.write_log(sessionID, "Bot Says: "+fulfillmentText)
        return {
            "fulfillmentText": fulfillmentText
        }
    else:
        #log.write_log(sessionID, "Bot Says: " + result.fulfillmentText)
        print("Hey I'm sorry something went wrong")


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')