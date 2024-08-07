from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# URL of your deployed model function
PREDICT_URL = "https://us-central1-valued-context-427614-g4.cloudfunctions.net/predict"

@app.route('/') # This route for the home page of the application.
def home():
    return render_template('index.html') # Rendering the HTML templates. 

@app.route('/predict', methods=['POST']) # This route for the prediction endpoint.
def predict():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':    # Checks if a file was selected ?
        return "No selected file", 400

    files = {'file': file.read()}
    response = requests.post(PREDICT_URL, files=files) # Sending the File to the Prediction URL.

    #H andling the Response
    if response.status_code != 200:
        return f"Prediction failed with status code {response.status_code}", 500
    
    # Returning the Prediction Result
    result = response.json()
    return jsonify(result) # Converts the result to a JSON response and returns it to the client.

if __name__ == '__main__':
    app.run(debug=True)




'''
Summary-
Home Page: Displays an HTML form for uploading an image (handled by home() and index.html).
Prediction Endpoint:
Receives the uploaded image.
Sends the image to the deployed model for prediction.
Returns the prediction result as a JSON response.
Error Handling: Ensures proper error messages are returned if the file is not present or if the prediction request fails.
'''
