"""
================================================================================
FLASK PREDICTION SERVICE - SOLAR IRRADIANCE PREDICTION
================================================================================
Project: Intelligent Solar Energy Analytics & Prediction System
Role: Machine Learning Engineer
Organization: Emmvee Solar Systems Pvt. Ltd.

Purpose: REST API for solar irradiance prediction
Endpoint: POST /predict
================================================================================
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

# ============================================================================
# INITIALIZE FLASK APP
# ============================================================================

app = Flask(__name__)

# Enable CORS to allow frontend requests
CORS(app)

# ============================================================================
# LOAD TRAINED MODEL AND SCALER
# ============================================================================

print("Loading trained model and scaler...")

try:
    # Load the trained Random Forest model
    model = joblib.load('random_forest_model.pkl')
    print("✓ Model loaded successfully")
    
    # Load the StandardScaler
    scaler = joblib.load('scaler.pkl')
    print("✓ Scaler loaded successfully")
    
except Exception as e:
    print(f"✗ Error loading model or scaler: {str(e)}")
    model = None
    scaler = None

# Define feature order (must match training data)
FEATURE_ORDER = ['temperature', 'cloud_cover', 'humidity', 'hour', 'month']

# ============================================================================
# HEALTH CHECK ENDPOINT
# ============================================================================

@app.route('/', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify service is running
    """
    return jsonify({
        'status': 'running',
        'service': 'Solar Irradiance Prediction API',
        'model': 'Random Forest Regressor',
        'version': '1.0'
    })

# ============================================================================
# PREDICTION ENDPOINT
# ============================================================================

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict solar irradiance based on input features
    
    Expected JSON input:
    {
        "temperature": float,
        "cloud_cover": float,
        "humidity": float,
        "hour": int,
        "month": int
    }
    
    Returns JSON output:
    {
        "predicted_solar_irradiance": float
    }
    """
    
    try:
        # ====================================================================
        # STEP 1: VALIDATE REQUEST
        # ====================================================================
        
        # Check if request contains JSON data
        if not request.is_json:
            return jsonify({
                'error': 'Request must be JSON',
                'status': 'failed'
            }), 400
        
        # Get JSON data from request
        data = request.get_json()
        
        # ====================================================================
        # STEP 2: EXTRACT AND VALIDATE INPUT FEATURES
        # ====================================================================
        
        # Check if all required features are present
        missing_features = [f for f in FEATURE_ORDER if f not in data]
        if missing_features:
            return jsonify({
                'error': f'Missing required features: {", ".join(missing_features)}',
                'status': 'failed'
            }), 400
        
        # Extract features in correct order
        try:
            features = [
                float(data['temperature']),
                float(data['cloud_cover']),
                float(data['humidity']),
                int(data['hour']),
                int(data['month'])
            ]
        except (ValueError, TypeError) as e:
            return jsonify({
                'error': f'Invalid feature values: {str(e)}',
                'status': 'failed'
            }), 400
        
        # ====================================================================
        # STEP 3: VALIDATE FEATURE RANGES
        # ====================================================================
        
        # Validate temperature (-10 to 50°C)
        if not -10 <= features[0] <= 50:
            return jsonify({
                'error': 'Temperature must be between -10°C and 50°C',
                'status': 'failed'
            }), 400
        
        # Validate cloud cover (0 to 100%)
        if not 0 <= features[1] <= 100:
            return jsonify({
                'error': 'Cloud cover must be between 0% and 100%',
                'status': 'failed'
            }), 400
        
        # Validate humidity (0 to 100%)
        if not 0 <= features[2] <= 100:
            return jsonify({
                'error': 'Humidity must be between 0% and 100%',
                'status': 'failed'
            }), 400
        
        # Validate hour (0 to 23)
        if not 0 <= features[3] <= 23:
            return jsonify({
                'error': 'Hour must be between 0 and 23',
                'status': 'failed'
            }), 400
        
        # Validate month (1 to 12)
        if not 1 <= features[4] <= 12:
            return jsonify({
                'error': 'Month must be between 1 and 12',
                'status': 'failed'
            }), 400
        
        # ====================================================================
        # STEP 4: SCALE FEATURES
        # ====================================================================
        
        # Convert to numpy array and reshape for scaler
        features_array = np.array(features).reshape(1, -1)
        
        # Apply StandardScaler transformation
        features_scaled = scaler.transform(features_array)
        
        # ====================================================================
        # STEP 5: MAKE PREDICTION
        # ====================================================================
        
        # Use trained model to predict solar irradiance
        prediction = model.predict(features_scaled)
        
        # Extract prediction value (convert from array to float)
        predicted_value = float(prediction[0])
        
        # Ensure prediction is non-negative (solar irradiance cannot be negative)
        predicted_value = max(0.0, predicted_value)
        
        # ====================================================================
        # STEP 6: RETURN PREDICTION
        # ====================================================================
        
        return jsonify({
            'predicted_solar_irradiance': round(predicted_value, 2),
            'unit': 'W/m²',
            'status': 'success',
            'input_features': {
                'temperature': features[0],
                'cloud_cover': features[1],
                'humidity': features[2],
                'hour': features[3],
                'month': features[4]
            }
        }), 200
    
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            'error': f'Prediction failed: {str(e)}',
            'status': 'failed'
        }), 500

# ============================================================================
# MODEL INFO ENDPOINT
# ============================================================================

@app.route('/model-info', methods=['GET'])
def model_info():
    """
    Get information about the loaded model
    """
    return jsonify({
        'model_type': 'Random Forest Regressor',
        'n_estimators': 100,
        'features': FEATURE_ORDER,
        'target': 'solar_irradiance',
        'unit': 'W/m²',
        'status': 'ready'
    })

# ============================================================================
# RUN FLASK APP
# ============================================================================

if __name__ == '__main__':
    print("\n" + "="*80)
    print("SOLAR IRRADIANCE PREDICTION API")
    print("="*80)
    print("\nEndpoints:")
    print("  GET  /           - Health check")
    print("  POST /predict    - Predict solar irradiance")
    print("  GET  /model-info - Model information")
    print("\n" + "="*80)
    print("Starting Flask server...")
    print("="*80 + "\n")
    
    # Run Flask app
    # debug=True enables auto-reload during development
    # host='0.0.0.0' makes server accessible from other devices
    app.run(debug=True, host='0.0.0.0', port=5000)
