# Solar Irradiance Prediction API

## Overview
Flask-based REST API for predicting solar irradiance using a trained Random Forest Regressor model.

## Files
- `app.py` - Flask application with prediction endpoint
- `random_forest_model.pkl` - Trained Random Forest model
- `scaler.pkl` - StandardScaler for feature normalization
- `test_api.py` - Test script with sample requests
- `requirements.txt` - Python dependencies

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the API

1. Start the Flask server:
```bash
python app.py
```

2. The API will be available at: `http://localhost:5000`

## API Endpoints

### 1. Health Check
```
GET /
```
Returns service status and information.

### 2. Predict Solar Irradiance
```
POST /predict
```

**Request Body (JSON):**
```json
{
    "temperature": 28.5,
    "cloud_cover": 15.0,
    "humidity": 45.0,
    "hour": 12,
    "month": 6
}
```

**Response (JSON):**
```json
{
    "predicted_solar_irradiance": 850.25,
    "unit": "W/m²",
    "status": "success",
    "input_features": {
        "temperature": 28.5,
        "cloud_cover": 15.0,
        "humidity": 45.0,
        "hour": 12,
        "month": 6
    }
}
```

### 3. Model Information
```
GET /model-info
```
Returns information about the loaded model.

## Input Features

| Feature | Type | Range | Description |
|---------|------|-------|-------------|
| temperature | float | -10 to 50 | Temperature in °C |
| cloud_cover | float | 0 to 100 | Cloud coverage percentage |
| humidity | float | 0 to 100 | Relative humidity percentage |
| hour | int | 0 to 23 | Hour of day (24-hour format) |
| month | int | 1 to 12 | Month of year |

## Testing

Run the test script:
```bash
python test_api.py
```

This will send sample requests to the API and display responses.

## Error Handling

The API returns appropriate HTTP status codes:
- `200` - Success
- `400` - Bad request (missing/invalid input)
- `500` - Server error

## Example Usage (Python)

```python
import requests

url = "http://localhost:5000/predict"
data = {
    "temperature": 28.5,
    "cloud_cover": 15.0,
    "humidity": 45.0,
    "hour": 12,
    "month": 6
}

response = requests.post(url, json=data)
print(response.json())
```

## Example Usage (cURL)

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "temperature": 28.5,
    "cloud_cover": 15.0,
    "humidity": 45.0,
    "hour": 12,
    "month": 6
  }'
```

## Notes

- CORS is enabled to allow frontend requests
- All predictions are non-negative (solar irradiance ≥ 0)
- Input validation ensures data quality
- Model uses StandardScaler for feature normalization
