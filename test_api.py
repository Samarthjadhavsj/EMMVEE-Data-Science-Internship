"""
================================================================================
TEST FLASK PREDICTION API
================================================================================
Project: Intelligent Solar Energy Analytics & Prediction System
Purpose: Test the Flask prediction service with sample requests
================================================================================
"""

import requests
import json

# API endpoint
API_URL = "http://localhost:5000/predict"

print("="*80)
print("TESTING SOLAR IRRADIANCE PREDICTION API")
print("="*80)
print()

# ============================================================================
# TEST CASE 1: SUNNY DAY CONDITIONS
# ============================================================================

print("TEST CASE 1: Sunny Day Conditions")
print("-"*80)

test_data_1 = {
    "temperature": 28.5,
    "cloud_cover": 15.0,
    "humidity": 45.0,
    "hour": 12,
    "month": 6
}

print("Input:")
print(json.dumps(test_data_1, indent=2))
print()

try:
    response = requests.post(API_URL, json=test_data_1)
    print(f"Status Code: {response.status_code}")
    print("Response:")
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"Error: {str(e)}")

print()

# ============================================================================
# TEST CASE 2: CLOUDY DAY CONDITIONS
# ============================================================================

print("TEST CASE 2: Cloudy Day Conditions")
print("-"*80)

test_data_2 = {
    "temperature": 22.0,
    "cloud_cover": 85.0,
    "humidity": 70.0,
    "hour": 14,
    "month": 3
}

print("Input:")
print(json.dumps(test_data_2, indent=2))
print()

try:
    response = requests.post(API_URL, json=test_data_2)
    print(f"Status Code: {response.status_code}")
    print("Response:")
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"Error: {str(e)}")

print()

# ============================================================================
# TEST CASE 3: NIGHT TIME (NO SOLAR IRRADIANCE)
# ============================================================================

print("TEST CASE 3: Night Time")
print("-"*80)

test_data_3 = {
    "temperature": 18.0,
    "cloud_cover": 50.0,
    "humidity": 60.0,
    "hour": 22,
    "month": 9
}

print("Input:")
print(json.dumps(test_data_3, indent=2))
print()

try:
    response = requests.post(API_URL, json=test_data_3)
    print(f"Status Code: {response.status_code}")
    print("Response:")
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"Error: {str(e)}")

print()

# ============================================================================
# TEST CASE 4: INVALID INPUT (MISSING FEATURE)
# ============================================================================

print("TEST CASE 4: Invalid Input (Missing Feature)")
print("-"*80)

test_data_4 = {
    "temperature": 25.0,
    "cloud_cover": 30.0,
    "humidity": 55.0,
    "hour": 10
    # Missing 'month' field
}

print("Input:")
print(json.dumps(test_data_4, indent=2))
print()

try:
    response = requests.post(API_URL, json=test_data_4)
    print(f"Status Code: {response.status_code}")
    print("Response:")
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"Error: {str(e)}")

print()

print("="*80)
print("API TESTING COMPLETE")
print("="*80)
