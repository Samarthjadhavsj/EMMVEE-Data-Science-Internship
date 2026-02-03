"""
================================================================================
COMPREHENSIVE TESTING SUITE - SOLAR IRRADIANCE PREDICTION SYSTEM
================================================================================
Project: Intelligent Solar Energy Analytics & Prediction System
Organization: Emmvee Solar Systems Pvt. Ltd.

This script tests all possible scenarios for the prediction system
================================================================================
"""

import requests
import json
import time

API_URL = "http://localhost:5000/predict"
HEALTH_URL = "http://localhost:5000/"
MODEL_INFO_URL = "http://localhost:5000/model-info"

def print_header(title):
    """Print formatted section header"""
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80)

def print_test(test_name, test_num, total):
    """Print test case header"""
    print(f"\n[TEST {test_num}/{total}] {test_name}")
    print("-" * 80)

def test_api_health():
    """Test 1: API Health Check"""
    print_header("PART 1: API CONNECTIVITY TESTS")
    
    print_test("Health Check Endpoint", 1, 3)
    try:
        response = requests.get(HEALTH_URL, timeout=5)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        if response.status_code == 200:
            print("✓ API is running")
            return True
        else:
            print("✗ API returned unexpected status")
            return False
    except Exception as e:
        print(f"✗ Cannot connect to API: {str(e)}")
        return False

def test_model_info():
    """Test 2: Model Info Endpoint"""
    print_test("Model Info Endpoint", 2, 3)
    try:
        response = requests.get(MODEL_INFO_URL, timeout=5)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        if response.status_code == 200:
            print("✓ Model info retrieved")
            return True
        else:
            print("✗ Failed to get model info")
            return False
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False

def test_cors():
    """Test 3: CORS Configuration"""
    print_test("CORS Headers Check", 3, 3)
    try:
        response = requests.options(API_URL, timeout=5)
        print(f"Status Code: {response.status_code}")
        print(f"CORS Headers: {dict(response.headers)}")
        if 'Access-Control-Allow-Origin' in response.headers:
            print("✓ CORS is properly configured")
            return True
        else:
            print("⚠ CORS headers not found")
            return False
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False

def test_valid_predictions():
    """Test 4-15: Valid Prediction Scenarios"""
    print_header("PART 2: VALID PREDICTION SCENARIOS")
    
    test_cases = [
        {
            "name": "Peak Summer Noon (Clear Sky)",
            "data": {"temperature": 35, "cloud_cover": 10, "humidity": 40, "hour": 12, "month": 6},
            "expected": "High irradiance (>400 W/m²)"
        },
        {
            "name": "Winter Morning (Partly Cloudy)",
            "data": {"temperature": 15, "cloud_cover": 50, "humidity": 70, "hour": 9, "month": 12},
            "expected": "Moderate irradiance"
        },
        {
            "name": "Monsoon Afternoon (Heavy Clouds)",
            "data": {"temperature": 25, "cloud_cover": 90, "humidity": 85, "hour": 14, "month": 7},
            "expected": "Low irradiance (<100 W/m²)"
        },
        {
            "name": "Night Time (Midnight)",
            "data": {"temperature": 20, "cloud_cover": 50, "humidity": 60, "hour": 0, "month": 5},
            "expected": "Zero irradiance"
        },
        {
            "name": "Early Morning (Sunrise)",
            "data": {"temperature": 18, "cloud_cover": 30, "humidity": 75, "hour": 6, "month": 3},
            "expected": "Low irradiance"
        },
        {
            "name": "Late Evening (Sunset)",
            "data": {"temperature": 22, "cloud_cover": 40, "humidity": 65, "hour": 18, "month": 8},
            "expected": "Low to zero irradiance"
        },
        {
            "name": "Spring Afternoon (Clear)",
            "data": {"temperature": 28, "cloud_cover": 15, "humidity": 50, "hour": 15, "month": 4},
            "expected": "High irradiance"
        },
        {
            "name": "Fall Morning (Foggy)",
            "data": {"temperature": 16, "cloud_cover": 70, "humidity": 90, "hour": 8, "month": 10},
            "expected": "Low irradiance"
        },
        {
            "name": "Extreme Heat (Clear Sky)",
            "data": {"temperature": 45, "cloud_cover": 5, "humidity": 20, "hour": 13, "month": 5},
            "expected": "Very high irradiance"
        },
        {
            "name": "Cold Winter Night",
            "data": {"temperature": 5, "cloud_cover": 60, "humidity": 80, "hour": 22, "month": 1},
            "expected": "Zero irradiance"
        },
        {
            "name": "Boundary: Min Temperature",
            "data": {"temperature": -10, "cloud_cover": 50, "humidity": 60, "hour": 12, "month": 1},
            "expected": "Variable irradiance"
        },
        {
            "name": "Boundary: Max Temperature",
            "data": {"temperature": 50, "cloud_cover": 20, "humidity": 30, "hour": 13, "month": 6},
            "expected": "High irradiance"
        }
    ]
    
    passed = 0
    for i, test in enumerate(test_cases, 1):
        print_test(test["name"], i+3, 15)
        print(f"Input: {json.dumps(test['data'], indent=2)}")
        print(f"Expected: {test['expected']}")
        
        try:
            response = requests.post(API_URL, json=test["data"], timeout=5)
            print(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                irradiance = result['predicted_solar_irradiance']
                print(f"Predicted: {irradiance} W/m²")
                print(f"✓ Prediction successful")
                passed += 1
            else:
                print(f"✗ Prediction failed: {response.json()}")
        except Exception as e:
            print(f"✗ Error: {str(e)}")
        
        time.sleep(0.1)  # Small delay between requests
    
    print(f"\n{'='*80}")
    print(f"Valid Predictions: {passed}/{len(test_cases)} passed")
    return passed == len(test_cases)

def test_invalid_inputs():
    """Test 16-25: Invalid Input Scenarios"""
    print_header("PART 3: INVALID INPUT VALIDATION")
    
    test_cases = [
        {
            "name": "Missing Temperature",
            "data": {"cloud_cover": 30, "humidity": 60, "hour": 12, "month": 6},
            "expected_error": "Missing required features"
        },
        {
            "name": "Missing Cloud Cover",
            "data": {"temperature": 25, "humidity": 60, "hour": 12, "month": 6},
            "expected_error": "Missing required features"
        },
        {
            "name": "Missing Humidity",
            "data": {"temperature": 25, "cloud_cover": 30, "hour": 12, "month": 6},
            "expected_error": "Missing required features"
        },
        {
            "name": "Missing Hour",
            "data": {"temperature": 25, "cloud_cover": 30, "humidity": 60, "month": 6},
            "expected_error": "Missing required features"
        },
        {
            "name": "Missing Month",
            "data": {"temperature": 25, "cloud_cover": 30, "humidity": 60, "hour": 12},
            "expected_error": "Missing required features"
        },
        {
            "name": "Invalid Temperature (Too Low)",
            "data": {"temperature": -20, "cloud_cover": 30, "humidity": 60, "hour": 12, "month": 6},
            "expected_error": "Temperature must be between"
        },
        {
            "name": "Invalid Temperature (Too High)",
            "data": {"temperature": 60, "cloud_cover": 30, "humidity": 60, "hour": 12, "month": 6},
            "expected_error": "Temperature must be between"
        },
        {
            "name": "Invalid Cloud Cover (Negative)",
            "data": {"temperature": 25, "cloud_cover": -10, "humidity": 60, "hour": 12, "month": 6},
            "expected_error": "Cloud cover must be between"
        },
        {
            "name": "Invalid Cloud Cover (>100)",
            "data": {"temperature": 25, "cloud_cover": 150, "humidity": 60, "hour": 12, "month": 6},
            "expected_error": "Cloud cover must be between"
        },
        {
            "name": "Invalid Humidity (Negative)",
            "data": {"temperature": 25, "cloud_cover": 30, "humidity": -5, "hour": 12, "month": 6},
            "expected_error": "Humidity must be between"
        },
        {
            "name": "Invalid Humidity (>100)",
            "data": {"temperature": 25, "cloud_cover": 30, "humidity": 120, "hour": 12, "month": 6},
            "expected_error": "Humidity must be between"
        },
        {
            "name": "Invalid Hour (Negative)",
            "data": {"temperature": 25, "cloud_cover": 30, "humidity": 60, "hour": -1, "month": 6},
            "expected_error": "Hour must be between"
        },
        {
            "name": "Invalid Hour (>23)",
            "data": {"temperature": 25, "cloud_cover": 30, "humidity": 60, "hour": 25, "month": 6},
            "expected_error": "Hour must be between"
        },
        {
            "name": "Invalid Month (Zero)",
            "data": {"temperature": 25, "cloud_cover": 30, "humidity": 60, "hour": 12, "month": 0},
            "expected_error": "Month must be between"
        },
        {
            "name": "Invalid Month (>12)",
            "data": {"temperature": 25, "cloud_cover": 30, "humidity": 60, "hour": 12, "month": 13},
            "expected_error": "Month must be between"
        },
        {
            "name": "Non-JSON Request",
            "data": "invalid_string",
            "expected_error": "Request must be JSON"
        },
        {
            "name": "Empty Request",
            "data": {},
            "expected_error": "Missing required features"
        },
        {
            "name": "String Instead of Number",
            "data": {"temperature": "hot", "cloud_cover": 30, "humidity": 60, "hour": 12, "month": 6},
            "expected_error": "Invalid feature values"
        }
    ]
    
    passed = 0
    for i, test in enumerate(test_cases, 1):
        print_test(test["name"], i+15, 33)
        print(f"Input: {test['data']}")
        print(f"Expected Error: {test['expected_error']}")
        
        try:
            if isinstance(test["data"], str):
                response = requests.post(API_URL, data=test["data"], timeout=5)
            else:
                response = requests.post(API_URL, json=test["data"], timeout=5)
            
            print(f"Status Code: {response.status_code}")
            
            if response.status_code in [400, 500]:
                result = response.json()
                error_msg = result.get('error', '')
                print(f"Error Message: {error_msg}")
                
                if test['expected_error'].lower() in error_msg.lower():
                    print(f"✓ Validation working correctly")
                    passed += 1
                else:
                    print(f"⚠ Different error than expected")
            else:
                print(f"✗ Should have returned error status")
        except Exception as e:
            print(f"✗ Error: {str(e)}")
        
        time.sleep(0.1)
    
    print(f"\n{'='*80}")
    print(f"Invalid Input Tests: {passed}/{len(test_cases)} passed")
    return passed == len(test_cases)

def test_dropdown_values():
    """Test 34-41: Dropdown Values from Form"""
    print_header("PART 4: FORM DROPDOWN VALUES")
    
    # Test all humidity dropdown options
    humidity_values = [20, 30, 40, 50, 60, 70, 80, 90]
    
    print_test("All Humidity Dropdown Options", 34, 41)
    passed = 0
    for humidity in humidity_values:
        data = {"temperature": 25, "cloud_cover": 30, "humidity": humidity, "hour": 12, "month": 6}
        try:
            response = requests.post(API_URL, json=data, timeout=5)
            if response.status_code == 200:
                result = response.json()
                print(f"  Humidity {humidity}%: {result['predicted_solar_irradiance']} W/m² ✓")
                passed += 1
            else:
                print(f"  Humidity {humidity}%: Failed ✗")
        except Exception as e:
            print(f"  Humidity {humidity}%: Error ✗")
    
    # Test sample hours (AM/PM format)
    print_test("Sample Hour Dropdown Options", 35, 41)
    hours = [0, 6, 12, 18, 23]  # Midnight, 6 AM, Noon, 6 PM, 11 PM
    hour_labels = ["12:00 AM", "6:00 AM", "12:00 PM", "6:00 PM", "11:00 PM"]
    
    for hour, label in zip(hours, hour_labels):
        data = {"temperature": 25, "cloud_cover": 30, "humidity": 60, "hour": hour, "month": 6}
        try:
            response = requests.post(API_URL, json=data, timeout=5)
            if response.status_code == 200:
                result = response.json()
                print(f"  {label}: {result['predicted_solar_irradiance']} W/m² ✓")
                passed += 1
            else:
                print(f"  {label}: Failed ✗")
        except Exception as e:
            print(f"  {label}: Error ✗")
    
    # Test all months
    print_test("All Month Dropdown Options", 36, 41)
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    
    for month_num, month_name in enumerate(months, 1):
        data = {"temperature": 25, "cloud_cover": 30, "humidity": 60, "hour": 12, "month": month_num}
        try:
            response = requests.post(API_URL, json=data, timeout=5)
            if response.status_code == 200:
                result = response.json()
                print(f"  {month_name}: {result['predicted_solar_irradiance']} W/m² ✓")
                passed += 1
            else:
                print(f"  {month_name}: Failed ✗")
        except Exception as e:
            print(f"  {month_name}: Error ✗")
    
    total_tests = len(humidity_values) + len(hours) + len(months)
    print(f"\n{'='*80}")
    print(f"Dropdown Tests: {passed}/{total_tests} passed")
    return passed == total_tests

def test_performance():
    """Test 42: Performance & Load Testing"""
    print_header("PART 5: PERFORMANCE TESTING")
    
    print_test("Response Time Test (10 requests)", 42, 43)
    
    test_data = {"temperature": 25, "cloud_cover": 30, "humidity": 60, "hour": 12, "month": 6}
    response_times = []
    
    for i in range(10):
        start_time = time.time()
        try:
            response = requests.post(API_URL, json=test_data, timeout=5)
            end_time = time.time()
            response_time = (end_time - start_time) * 1000  # Convert to ms
            response_times.append(response_time)
            print(f"  Request {i+1}: {response_time:.2f} ms")
        except Exception as e:
            print(f"  Request {i+1}: Failed")
    
    if response_times:
        avg_time = sum(response_times) / len(response_times)
        min_time = min(response_times)
        max_time = max(response_times)
        
        print(f"\nPerformance Summary:")
        print(f"  Average: {avg_time:.2f} ms")
        print(f"  Minimum: {min_time:.2f} ms")
        print(f"  Maximum: {max_time:.2f} ms")
        
        if avg_time < 1000:  # Less than 1 second
            print(f"✓ Performance is good")
            return True
        else:
            print(f"⚠ Performance could be improved")
            return False
    return False

def test_concurrent_requests():
    """Test 43: Concurrent Request Handling"""
    print_test("Concurrent Requests Test", 43, 43)
    
    import concurrent.futures
    
    def make_request(i):
        data = {"temperature": 20 + i, "cloud_cover": 30, "humidity": 60, "hour": 12, "month": 6}
        try:
            response = requests.post(API_URL, json=data, timeout=5)
            return response.status_code == 200
        except:
            return False
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(make_request, i) for i in range(5)]
        results = [f.result() for f in concurrent.futures.as_completed(futures)]
    
    passed = sum(results)
    print(f"Concurrent requests: {passed}/5 successful")
    
    if passed == 5:
        print("✓ API handles concurrent requests well")
        return True
    else:
        print("⚠ Some concurrent requests failed")
        return False

def run_all_tests():
    """Run complete test suite"""
    print("\n" + "="*80)
    print("  COMPREHENSIVE TESTING SUITE")
    print("  Solar Irradiance Prediction System")
    print("  Emmvee Solar Systems Pvt. Ltd.")
    print("="*80)
    
    results = {
        "API Health": test_api_health(),
        "Model Info": test_model_info(),
        "CORS": test_cors(),
        "Valid Predictions": test_valid_predictions(),
        "Invalid Inputs": test_invalid_inputs(),
        "Dropdown Values": test_dropdown_values(),
        "Performance": test_performance(),
        "Concurrent Requests": test_concurrent_requests()
    }
    
    # Final Summary
    print_header("FINAL TEST SUMMARY")
    
    total_passed = sum(results.values())
    total_tests = len(results)
    
    for test_name, passed in results.items():
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{test_name:.<50} {status}")
    
    print("\n" + "="*80)
    print(f"OVERALL RESULT: {total_passed}/{total_tests} test categories passed")
    
    if total_passed == total_tests:
        print("✓ ALL TESTS PASSED - System is production ready!")
    else:
        print("⚠ Some tests failed - Review issues above")
    
    print("="*80 + "\n")

if __name__ == "__main__":
    run_all_tests()
