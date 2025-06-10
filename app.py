import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os

# Create flask app
flask_app = Flask(__name__)

# Load model and preprocessors
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
le1 = pickle.load(open("le1.pkl", "rb"))
le2 = pickle.load(open("le2.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route('/predict', methods=['GET'])
def predict_get():
    # Redirect GET requests to home page
    return render_template('index.html')

@flask_app.route("/predict", methods = ["POST"])
def predict():
    # Get form values as a list
    form_values = list(request.form.values())
    # Apply label encoding to the correct features (assuming feature2 and feature5 are categorical)
    # Adjust indices if your form order is different
    form_values[1] = le1.transform([form_values[1]])[0] if not form_values[1].isdigit() else int(form_values[1])
    form_values[4] = le2.transform([form_values[4]])[0] if not form_values[4].isdigit() else int(form_values[4])
    # Convert all to float
    float_features = [float(x) for x in form_values]
    # Scale features
    features = scaler.transform([float_features])
    prediction = model.predict(features)
    if prediction[0] == 1:
        prediction = "introvert"
    else:
        prediction = "extrovert"
    return render_template("index.html", prediction_text = f"you are {prediction}")

if __name__ == "__main__":
    flask_app.run(host = '0.0.0.0',debug=True)