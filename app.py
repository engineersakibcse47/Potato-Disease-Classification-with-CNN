from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# URL of your deployed model function
PREDICT_URL = "https://us-central1-valued-context-427614-g4.cloudfunctions.net/predict"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    files = {'file': file.read()}
    response = requests.post(PREDICT_URL, files=files)

    if response.status_code != 200:
        return f"Prediction failed with status code {response.status_code}", 500

    result = response.json()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
