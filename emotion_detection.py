import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type":"application/json"    
    }
    payload = {
        "raw_document":{
        "text": text_to_analyze
        }
    }
    try:
        response = requests.post(url, headers=headers, json = payload)

        if response.status_code == 200:
            # return response.text
            jsonObj = json.load(response.text)
            return jsonObj["emotionPredictions"][0]["emotion"]
        else:
            return f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Request failed: {str(e)}"

text = emotion_detector("I love this new technology.")


