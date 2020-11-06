import json

reques= {
  "responseId": "b84733b6-7ca2-4c86-a794-40aea39779fa-ee7586fb",
  "queryResult": {
    "queryText": "what is speech",
    "parameters": {
      "Question": "what is speech"
    },
    "allRequiredParamsPresent": 2,
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
    "enableAgentWideTts": 1
  }
}
data = json.loads(reques)

#r= json.load(reques)
print(data)