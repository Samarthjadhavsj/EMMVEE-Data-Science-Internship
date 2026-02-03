# Complete Testing Guide - Solar Irradiance Prediction System

## Overview
This guide covers all possible ways to test your solar prediction system, including automated tests, manual browser tests, and edge case scenarios.

---

## Method 1: Automated API Testing (Recommended First)

### Run Comprehensive Test Suite
```bash
python comprehensive_test.py
```

**What it tests:**
- ✓ API connectivity and health
- ✓ Model information endpoint
- ✓ CORS configuration
- ✓ 12 valid prediction scenarios (summer, winter, day, night, etc.)
- ✓ 18 invalid input validations
- ✓ All dropdown values (8 humidity + 24 hours + 12 months)
- ✓ Performance testing (response times)
- ✓ Concurrent request handling

**Expected Result:** All 43 tests should pass

---

## Method 2: Manual Browser Testing

### Step 1: Start the Flask API
```bash
python app.py
```
**Expected:** Server running at http://localhost:5000

### Step 2: Open the Website
1. Open `index.html` in your browser
2. Click on "Prediction" in navigation

### Step 3: Test Form Functionality

#### Test Case 1: Default Values (Sunny Day)
- Temperature: 25°C
- Cloud Cover: 30%
- Humidity: Moderate-High (60%)
- Time: 12:00 PM (Noon)
- Month: June
- **Expected Result:** ~400-450 W/m²

#### Test Case 2: Clear Summer Day
- Temperature: 35°C
- Cloud Cover: 10%
- Humidity: Very Low (20%)
- Time: 1:00 PM
- Month: May
- **Expected Result:** >500 W/m² (High irradiance)

#### Test Case 3: Cloudy Day
- Temperature: 22°C
- Cloud Cover: 85%
- Humidity: Very High (80%)
- Time: 2:00 PM
- Month: July
- **Expected Result:** <100 W/m² (Low irradiance)

#### Test Case 4: Night Time
- Temperature: 18°C
- Cloud Cover: 50%
- Humidity: Moderate (50%)
- Time: 12:00 AM (Midnight)
- Month: Any
- **Expected Result:** 0 W/m² (Zero irradiance)

#### Test Case 5: Early Morning
- Temperature: 16°C
- Cloud Cover: 40%
- Humidity: High (70%)
- Time: 6:00 AM
- Month: March
- **Expected Result:** Low irradiance (50-150 W/m²)

#### Test Case 6: Late Evening
- Temperature: 20°C
- Cloud Cover: 30%
- Humidity: Moderate-High (60%)
- Time: 6:00 PM
- Month: September
- **Expected Result:** Very low to zero irradiance

#### Test Case 7: Winter Noon
- Temperature: 10°C
- Cloud Cover: 60%
- Humidity: Very High (80%)
- Time: 12:00 PM
- Month: December
- **Expected Result:** Moderate irradiance (200-300 W/m²)

---

## Method 3: Test All Dropdown Combinations

### Humidity Dropdown (8 options)
Test each humidity level with same other values:
- Very Low (20%)
- Low (30%)
- Moderate-Low (40%)
- Moderate (50%)
- Moderate-High (60%)
- High (70%)
- Very High (80%)
- Extremely High (90%)

**Expected:** Higher humidity generally reduces irradiance slightly

### Time of Day Dropdown (24 options)
Test key hours:
- **Night (12 AM - 5 AM):** Should predict 0 W/m²
- **Dawn (6 AM - 7 AM):** Low irradiance (50-150 W/m²)
- **Morning (8 AM - 11 AM):** Increasing irradiance
- **Noon (12 PM - 2 PM):** Peak irradiance (400-600+ W/m²)
- **Afternoon (3 PM - 5 PM):** Decreasing irradiance
- **Evening (6 PM - 7 PM):** Low irradiance
- **Night (8 PM - 11 PM):** Should predict 0 W/m²

### Month Dropdown (12 options)
Test seasonal variations:
- **Winter (Dec, Jan, Feb):** Lower irradiance
- **Spring (Mar, Apr, May):** Moderate to high
- **Summer (Jun, Jul, Aug):** Highest irradiance
- **Fall (Sep, Oct, Nov):** Moderate irradiance

---

## Method 4: Edge Case Testing

### Boundary Values

#### Temperature Boundaries
- Minimum: -10°C (extreme cold)
- Maximum: 50°C (extreme heat)
- **Test both with clear sky at noon**

#### Cloud Cover Boundaries
- Minimum: 0% (perfectly clear)
- Maximum: 100% (completely overcast)
- **Test at noon in summer**

#### Humidity Boundaries
- Minimum: 20% (very dry)
- Maximum: 90% (very humid)
- **Test with moderate cloud cover**

---

## Method 5: User Experience Testing

### Visual Tests
1. **Form Layout**
   - ✓ Form is centered and max-width 800px
   - ✓ All labels are visible and clear
   - ✓ Dropdowns show arrow icon
   - ✓ Input fields have units (°C, %)

2. **Interactive Effects**
   - ✓ Click on input → Blue glow appears
   - ✓ Hover over button → Color changes to #0077ED
   - ✓ Click button → Text changes to "Predicting..."
   - ✓ Button is disabled during prediction

3. **Result Display**
   - ✓ Result appears in large 56px font
   - ✓ Interpretation text is clear and helpful
   - ✓ Result box has light gray background

4. **Error Handling**
   - ✓ Stop Flask API and test → Should show connection error
   - ✓ Error message is clear and helpful

### Accessibility Tests
1. **Keyboard Navigation**
   - Tab through all form fields
   - Press Enter to submit form
   - All fields should be accessible

2. **Screen Reader**
   - All labels should be properly associated
   - Button text should be descriptive

---

## Method 6: API Direct Testing

### Using cURL (Command Line)

#### Test 1: Valid Prediction
```bash
curl -X POST http://localhost:5000/predict ^
  -H "Content-Type: application/json" ^
  -d "{\"temperature\": 25, \"cloud_cover\": 30, \"humidity\": 60, \"hour\": 12, \"month\": 6}"
```

#### Test 2: Missing Feature
```bash
curl -X POST http://localhost:5000/predict ^
  -H "Content-Type: application/json" ^
  -d "{\"temperature\": 25, \"cloud_cover\": 30, \"humidity\": 60, \"hour\": 12}"
```

#### Test 3: Invalid Range
```bash
curl -X POST http://localhost:5000/predict ^
  -H "Content-Type: application/json" ^
  -d "{\"temperature\": 100, \"cloud_cover\": 30, \"humidity\": 60, \"hour\": 12, \"month\": 6}"
```

### Using Python Requests
```python
import requests

# Test prediction
response = requests.post('http://localhost:5000/predict', json={
    "temperature": 25,
    "cloud_cover": 30,
    "humidity": 60,
    "hour": 12,
    "month": 6
})

print(response.json())
```

---

## Method 7: Performance Testing

### Response Time Test
Run the comprehensive test suite which includes:
- 10 sequential requests
- Average response time calculation
- **Expected:** <1000ms per request

### Load Test (Optional)
```python
import concurrent.futures
import requests

def make_request():
    return requests.post('http://localhost:5000/predict', json={
        "temperature": 25, "cloud_cover": 30, 
        "humidity": 60, "hour": 12, "month": 6
    })

# Test 50 concurrent requests
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(make_request) for _ in range(50)]
    results = [f.result() for f in futures]

print(f"Success rate: {sum(r.status_code == 200 for r in results)}/50")
```

---

## Method 8: Cross-Browser Testing

Test the website in multiple browsers:
- ✓ Google Chrome
- ✓ Mozilla Firefox
- ✓ Microsoft Edge
- ✓ Safari (if on Mac)

**What to check:**
- Form displays correctly
- Dropdowns work properly
- Button styling is consistent
- Results display correctly
- No console errors

---

## Method 9: Mobile Responsiveness Testing

### Desktop Browser Method
1. Open browser DevTools (F12)
2. Click device toolbar icon
3. Test different screen sizes:
   - iPhone SE (375px)
   - iPhone 12 Pro (390px)
   - iPad (768px)
   - Desktop (1920px)

**Expected:** Form should be readable and usable on all sizes

---

## Method 10: Error Scenario Testing

### Test API Offline
1. Stop Flask API (Ctrl+C)
2. Try to submit prediction form
3. **Expected:** Red error box with connection message

### Test Invalid Manual Input
1. Open browser console (F12)
2. Manually change input values in HTML
3. Try extreme values
4. **Expected:** API should reject with validation error

---

## Quick Test Checklist

### Before Deployment
- [ ] Run `python comprehensive_test.py` - All tests pass
- [ ] Test in browser with 5 different scenarios
- [ ] Test all dropdown options work
- [ ] Test night time returns 0 W/m²
- [ ] Test noon returns high irradiance
- [ ] Test error handling (stop API)
- [ ] Check form styling matches Apple design
- [ ] Test on mobile screen size
- [ ] Verify CORS is working
- [ ] Check API response times <1s

### Production Readiness
- [ ] All automated tests passing
- [ ] Manual browser tests successful
- [ ] No console errors
- [ ] Performance acceptable
- [ ] Error messages are user-friendly
- [ ] Form is accessible
- [ ] Works in multiple browsers

---

## Troubleshooting

### Issue: "Cannot connect to API"
**Solution:** Make sure Flask is running: `python app.py`

### Issue: "CORS error"
**Solution:** Verify flask-cors is installed: `pip install flask-cors`

### Issue: Predictions seem wrong
**Solution:** Check model and scaler files exist: `random_forest_model.pkl`, `scaler.pkl`

### Issue: Form doesn't submit
**Solution:** Check browser console (F12) for JavaScript errors

---

## Test Results Documentation

After testing, document:
1. Total tests run
2. Tests passed/failed
3. Any issues found
4. Browser compatibility
5. Performance metrics
6. User experience feedback

---

## Conclusion

Your system is production-ready when:
- ✓ All 43 automated tests pass
- ✓ Manual browser tests work correctly
- ✓ All dropdown combinations tested
- ✓ Edge cases handled properly
- ✓ Performance is acceptable (<1s response)
- ✓ Error handling works correctly
- ✓ Cross-browser compatible
- ✓ Mobile responsive

**Run the comprehensive test now:**
```bash
python comprehensive_test.py
```
