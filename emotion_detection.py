import requests
import json

import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    try:
        response = requests.post(url, json=myobj, headers=headers)
        response.raise_for_status()
        formatted_response = response.json()

        # Debug: print raw JSON response from Watson
        print(json.dumps(formatted_response, indent=4))

        # Extract emotion scores
        emotion_data = formatted_response.get("emotionPredictions", [{}])[0].get("emotion", {})
        
        if not emotion_data:
            return {"error": "No emotion data returned"}

        # Add dominant emotion
        dominant_emotion = max(emotion_data, key=emotion_data.get)
        emotion_data["dominant_emotion"] = dominant_emotion

        return emotion_data

    except Exception as e:
        print("API error:", e)
        return {"error": str(e)}

if response.status_code == 400:
        # Handle blank input (Bad Request)
        return {
            "sadness": None,
            "joy": None,
            "fear": None,
            "disgust": None,
            "anger": None,
            "dominant_emotion": None
        }

    formatted_response = response.json()
    emotion_data = formatted_response.get("emotionPredictions", [{}])[0].get("emotion", {})

    if not emotion_data:
        return {
            "sadness": None,
            "joy": None,
            "fear": None,
            "disgust": None,
            "anger": None,
            "dominant_emotion": None
        }

    dominant_emotion = max(emotion_data, key=emotion_data.get)
    emotion_data["dominant_emotion"] = dominant_emotion
    return emotion_data