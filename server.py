from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'Missing text field'}), 400

    result = emotion_detector(data['text'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)