from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text)

    return formatted_response

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'Missing text field'}), 400

    result = emotion_detector(data['text'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)