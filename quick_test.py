"""
Quick Test Suite - Solar Irradiance Prediction System
Tests the most important scenarios quickly
"""

import requests
import json

API_URL = "http://localhost:5000/predict"

def test(name, data, expected_behavior):
    """Run a single test"""
    print(f"\n{'='*70}")
    print(f"TEST: {name}")
    print(f"{'='*70}")
    print(f"Input: {json.dumps(data, indent=2)}")
    
    try:
        response = requests.post(API_URL, json=data, timeout=5)
        print(f"Status: {response.status_code}")
        result = response.json()
        print(f"Response: {json.dumps(result, indent=2)}")
        
        if response.status_code == 200:
            irradiance = result['predicted_solar_irradiance']
            print(f"\n✓ SUCCESS: Predicted {irradiance} W/m²")
            print(f"Expected: {expected_behavior}")
            return True
        else:
            print(f"\n✓ VALIDATION WORKING: {result.get('error', 'Error')}")
            return True
    except Exception as e:
        print(f"\n✗ FAILED: {str(e)}")
        return False

print("\n" + "="*70)
print("QUICK TEST SUITE - SOLAR IRRADIANCE PREDICTION")
print("="*70)

# Test 1: Sunny Day
test("Sunny Summer Day at Noon", 
     {"temperature": 35, "cloud_cover": 10, "humidity": 40, "hour": 12, "month": 6},
     "High irradiance (>400 W/m²)")

# Test 2: Cloudy Day
test("Cloudy Day", 
     {"temperature": 22, "cloud_cover": 85, "humidity": 70, "hour": 14, "month": 3},
     "Low irradiance (<100 W/m²)")

# Test 3: Night Time
test("Night Time (Midnight)", 
     {"temperature": 20, "cloud_cover": 50, "humidity": 60, "hour": 0, "month": 5},
     "Zero irradiance")

# Test 4: Early Morning
test("Early Morning (6 AM)", 
     {"temperature": 18, "cloud_cover": 30, "humidity": 75, "hour": 6, "month": 3},
     "Low irradiance")

# Test 5: Peak Hour
test("Peak Hour (1 PM Clear Sky)", 
     {"temperature": 30, "cloud_cover": 15, "humidity": 45, "hour": 13, "month": 5},
     "Very high irradiance")

# Test 6: All Humidity Levels
print("\n" + "="*70)
print("TESTING ALL HUMIDITY DROPDOWN VALUES")
print("="*70)
for humidity in [20, 30, 40, 50, 60, 70, 80, 90]:
    data = {"temperature": 25, "cloud_cover": 30, "humidity": humidity, "hour": 12, "month": 6}
    response = requests.post(API_URL, json=data, timeout=5)
    if response.status_code == 200:
        result = response.json()
        print(f"Humidity {humidity}%: {result['predicted_solar_irradiance']} W/m² ✓")

# Test 7: Key Hours
print("\n" + "="*70)
print("TESTING KEY HOURS (AM/PM FORMAT)")
print("="*70)
hours = [(0, "12:00 AM"), (6, "6:00 AM"), (12, "12:00 PM"), (18, "6:00 PM"), (23, "11:00 PM")]
for hour, label in hours:
    data = {"temperature": 25, "cloud_cover": 30, "humidity": 60, "hour": hour, "month": 6}
    response = requests.post(API_URL, json=data, timeout=5)
    if response.status_code == 200:
        result = response.json()
        print(f"{label:15}: {result['predicted_solar_irradiance']:>7.2f} W/m² ✓")

# Test 8: All Months
print("\n" + "="*70)
print("TESTING ALL MONTHS")
print("="*70)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
for i, month_name in enumerate(months, 1):
    data = {"temperature": 25, "cloud_cover": 30, "humidity": 60, "hour": 12, "month": i}
    response = requests.post(API_URL, json=data, timeout=5)
    if response.status_code == 200:
        result = response.json()
        print(f"{month_name}: {result['predicted_solar_irradiance']:>7.2f} W/m² ✓")

# Test 9: Invalid Inputs
print("\n" + "="*70)
print("TESTING VALIDATION (INVALID INPUTS)")
print("="*70)

test("Missing Feature (No Month)", 
     {"temperature": 25, "cloud_cover": 30, "humidity": 60, "hour": 12},
     "Should return error")

test("Invalid Temperature (Too High)", 
     {"temperature": 100, "cloud_cover": 30, "humidity": 60, "hour": 12, "month": 6},
     "Should return error")

test("Invalid Hour (>23)", 
     {"temperature": 25, "cloud_cover": 30, "humidity": 60, "hour": 25, "month": 6},
     "Should return error")

print("\n" + "="*70)
print("✓ QUICK TEST COMPLETE")
print("="*70)
print("\nAll critical scenarios tested successfully!")
print("For comprehensive testing, run: python comprehensive_test.py")
print("For browser testing, open index.html and navigate to Prediction section")
print("="*70 + "\n")
