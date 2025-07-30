import numpy as np
import pickle
import pandas as pd
from flask import Flask, request, render_template, flash, redirect, url_for
import logging

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the trained model
try:
    model = pickle.load(open('model.pkl', 'rb'))
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    model = None

# Define the order of expected input features
FEATURES = [
    'Gender', 'Age', 'History', 'Patient', 'TakeMedication', 'Severity',
    'BreathShortness', 'VisualChanges', 'NoseBleeding', 'Whendiagnoused',
    'Systolic', 'Diastolic', 'ControlledDiet'
]

# Label mapping for model output
label_map = {
    0: "NORMAL",
    1: "HYPERTENSION (Stage-1)",
    2: "HYPERTENSION (Stage-2)",
    3: "HYPERTENSIVE CRISIS"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_form')
def predict_form():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            return render_template('result.html', 
                                prediction_text="Error: Model not available. Please contact administrator.")
        
        # Extract and validate all form inputs
        features_values = []
        missing_fields = []
        
        for feature in FEATURES:
            value = request.form.get(feature)
            if value is None or value == '':
                missing_fields.append(feature)
            else:
                try:
                    features_values.append(float(value))
                except ValueError:
                    missing_fields.append(feature)
        
        if missing_fields:
            return render_template('result.html', 
                                prediction_text=f"Error: Missing or invalid values for: {', '.join(missing_fields)}")
        
        # Convert to numpy array and reshape
        features_array = np.array(features_values).reshape(1, -1)
        
        # Convert to DataFrame
        df = pd.DataFrame(features_array, columns=FEATURES)
        
        # Make prediction
        prediction = model.predict(df)
        result = label_map.get(prediction[0], "Unknown Result")
        
        logger.info(f"Prediction made successfully: {result}")
        return render_template('result.html', prediction_text=f"Your Blood Pressure stage is: {result}")
    
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return render_template('result.html', 
                            prediction_text="Error: An unexpected error occurred. Please try again.")

@app.errorhandler(404)
def not_found_error(error):
    return render_template('result.html', 
                         prediction_text="Error: Page not found. Please go back to the home page.")

@app.errorhandler(500)
def internal_error(error):
    return render_template('result.html', 
                         prediction_text="Error: Internal server error. Please try again later.")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
