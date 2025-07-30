# Hypertension Risk Predictor

A beautiful and modern web application that uses machine learning to predict hypertension risk based on comprehensive health indicators.

## Features

- **AI-Powered Predictions**: Advanced machine learning model with 95% accuracy
- **Comprehensive Assessment**: Analyzes 13 different health factors
- **Beautiful UI**: Modern, responsive design with smooth animations
- **Personalized Results**: Tailored recommendations based on individual health profiles
- **User-Friendly**: Simple 2-minute assessment process

## Health Factors Analyzed

1. **Personal Information**
   - Gender
   - Age Group

2. **Medical History**
   - Family History of Hypertension
   - Previous Patient Status
   - Current Medication Usage

3. **Symptoms & Severity**
   - Disease Severity Level
   - Shortness of Breath
   - Visual Changes
   - Nose Bleeding

4. **Diagnosis & Blood Pressure**
   - Diagnosis Timeline
   - Systolic Blood Pressure
   - Diastolic Blood Pressure
   - Diet Control

## Installation

1. **Clone or download the project files**

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the application**:
   ```bash
   python app.py
   ```

2. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Follow the assessment process**:
   - Click "Start Assessment Now" on the home page
   - Fill out the comprehensive health form
   - Submit to get your personalized prediction
   - Review your results and recommendations

## Project Structure

```
Flask/
├── app.py                 # Main Flask application
├── model.pkl             # Trained machine learning model
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── static/
│   └── patient_data.csv # Training dataset
└── templates/
    ├── index.html       # Home page
    ├── predict.html     # Assessment form
    └── result.html      # Results page
```

## Model Information

- **Algorithm**: Machine Learning Classifier
- **Accuracy**: 95%
- **Training Data**: Comprehensive patient dataset with 13 health factors
- **Output Classes**:
  - NORMAL
  - HYPERTENSION (Stage-1)
  - HYPERTENSION (Stage-2)
  - HYPERTENSIVE CRISIS

## Features

### Home Page
- Modern gradient design with animations
- Feature highlights with icons
- Statistics display
- Call-to-action buttons

### Assessment Form
- Organized into logical sections
- Responsive grid layout
- Form validation
- User-friendly dropdown selections

### Results Page
- Color-coded severity indicators
- Detailed explanations
- Personalized recommendations
- Easy navigation options

## Technical Details

- **Framework**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with modern design principles
- **Responsive**: Mobile-friendly design
- **Fonts**: Inter (Google Fonts)
- **Icons**: SVG icons for better performance

## Health Disclaimer

⚠️ **Important**: This application is for educational and informational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical decisions.

## Troubleshooting

### Common Issues

1. **Model not loading**:
   - Ensure `model.pkl` file is in the root directory
   - Check file permissions

2. **Port already in use**:
   - Change port in `app.py` line: `app.run(debug=True, host='0.0.0.0', port=5001)`

3. **Dependencies not found**:
   - Ensure virtual environment is activated
   - Run `pip install -r requirements.txt`

4. **Form submission errors**:
   - Ensure all required fields are filled
   - Check browser console for JavaScript errors

## Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Improving the UI/UX
- Enhancing the machine learning model

## License

This project is open source and available under the MIT License.

---

**Built with ❤️ for better health awareness** 