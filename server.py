from flask import Flask, request, jsonify, render_template
from emotion_detection import emotion_detector
import json
import requests


app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def detect_emotion():
    if request.method == 'GET':
        text = request.args.get('textToAnalyze', '')
    else:
        data = request.get_json()
        text = data.get('text', '') if data else ''

    if not text:
        return jsonify({'error': 'Missing text input'}), 400

    result = emotion_detector(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)


"""should be a combination of the above and below code"""
"""Flask-based API for emotion detection."""
from flask import Flask, request, jsonify, render_template
from final_project.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """default path for index page"""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def detect_emotion():
    """detect emotion method"""
    if request.method == 'GET':
        text = request.args.get('textToAnalyze', '')

    else:
        data = request.get_json()
        text = data.get('text', '') if data else ''

    result = emotion_detector(text)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)