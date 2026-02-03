# Visual Testing Guide - What You Should See

## 1. Starting the API

### Command:
```bash
python app.py
```

### Expected Output:
```
================================================================================
SOLAR IRRADIANCE PREDICTION API
================================================================================

Endpoints:
  GET  /           - Health check
  POST /predict    - Predict solar irradiance
  GET  /model-info - Model information

================================================================================
Starting Flask server...
================================================================================

Loading trained model and scaler...
✓ Model loaded successfully
✓ Scaler loaded successfully
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
 * Running on http://localhost:5000
```

✓ If you see this, API is ready!

---

## 2. Running Quick Test

### Command:
```bash
python quick_test.py
```

### Expected Output (Sample):
```
======================================================================
QUICK TEST SUITE - SOLAR IRRADIANCE PREDICTION
======================================================================

======================================================================
TEST: Sunny Summer Day at Noon
======================================================================
Input: {
  "temperature": 35,
  "cloud_cover": 10,
  "humidity": 40,
  "hour": 12,
  "month": 6
}
Status: 200
Response: {
  "predicted_solar_irradiance": 438.81,
  "status": "success",
  "unit": "W/m²"
}

✓ SUCCESS: Predicted 438.81 W/m²
Expected: High irradiance (>400 W/m²)

[... more tests ...]

======================================================================
TESTING ALL HUMIDITY DROPDOWN VALUES
======================================================================
Humidity 20%: 384.65 W/m² ✓
Humidity 30%: 391.06 W/m² ✓
Humidity 40%: 393.59 W/m² ✓
[... etc ...]

======================================================================
✓ QUICK TEST COMPLETE
======================================================================
```

✓ Look for all ✓ marks - means everything works!

---

## 3. Opening the Website

### Steps:
1. Double-click `index.html`
2. Browser opens automatically

### What You Should See:

```
┌─────────────────────────────────────────────────────────────┐
│  Profile | Data | Analysis | Insights | Prediction | Summary │ ← Navigation
└─────────────────────────────────────────────────────────────┘

    Intelligent Solar Energy Analytics & Prediction System
    
    ┌───────────────────────────────────────────────────┐
    │ Role: Data Science Intern                         │
    │ Organization: Emmvee Solar Systems Pvt. Ltd.      │
    └───────────────────────────────────────────────────┘
    
    [Project Overview section...]
```

✓ Clean, professional Apple-style design

---

## 4. Clicking "Prediction" Section

### What You Should See:

```
┌─────────────────────────────────────────────────────────────┐
│  Profile | Data | Analysis | Insights | PREDICTION | Summary │
└─────────────────────────────────────────────────────────────┘

                    Prediction
                    
        ┌─────────────────────────────────────────────┐
        │  Solar Irradiance Prediction                │
        │  Enter weather conditions to get            │
        │  real-time predictions.                     │
        │                                             │
        │  Temperature                                │
        │  ┌─────────────────────────────────────┐   │
        │  │ 30                              °C  │   │
        │  └─────────────────────────────────────┘   │
        │                                             │
        │  Cloud Cover                                │
        │  ┌─────────────────────────────────────┐   │
        │  │ 20                               %  │   │
        │  └─────────────────────────────────────┘   │
        │                                             │
        │  Humidity                                   │
        │  ┌─────────────────────────────────────┐   │
        │  │ Moderate-High (60%)             ▼  │   │
        │  └─────────────────────────────────────┘   │
        │                                             │
        │  Time of Day                                │
        │  ┌─────────────────────────────────────┐   │
        │  │ 12:00 PM (Noon)                 ▼  │   │
        │  └─────────────────────────────────────┘   │
        │                                             │
        │  Month                                      │
        │  ┌─────────────────────────────────────┐   │
        │  │ June                            ▼  │   │
        │  └─────────────────────────────────────┘   │
        │                                             │
        │  ┌─────────────────────────────────────┐   │
        │  │   Predict Solar Irradiance          │   │ ← Blue button
        │  └─────────────────────────────────────┘   │
        └─────────────────────────────────────────────┘
```

✓ Form centered, max-width 800px
✓ Clean white card with shadow
✓ All fields visible
✓ Dropdowns show arrow icons

---

## 5. Clicking on Input Field

### What You Should See:

```
Temperature
┌─────────────────────────────────────┐
│ 30                              °C  │ ← Blue glow around field
└─────────────────────────────────────┘
  ↑
  Blue border (#0071e3)
  Blue shadow (0 0 0 4px rgba(0, 113, 227, 0.1))
```

✓ Blue glow appears when field is focused
✓ Glow disappears when you click away

---

## 6. Opening Dropdown

### Humidity Dropdown:
```
Humidity
┌─────────────────────────────────────┐
│ Moderate-High (60%)             ▼  │ ← Click here
└─────────────────────────────────────┘
        ↓
┌─────────────────────────────────────┐
│ Very Low (20%)                      │
│ Low (30%)                           │
│ Moderate-Low (40%)                  │
│ Moderate (50%)                      │
│ Moderate-High (60%)            ✓    │ ← Currently selected
│ High (70%)                          │
│ Very High (80%)                     │
│ Extremely High (90%)                │
└─────────────────────────────────────┘
```

### Hour Dropdown:
```
Time of Day
┌─────────────────────────────────────┐
│ 12:00 PM (Noon)                 ▼  │
└─────────────────────────────────────┘
        ↓
┌─────────────────────────────────────┐
│ 12:00 AM (Midnight)                 │
│ 1:00 AM                             │
│ 2:00 AM                             │
│ ...                                 │
│ 12:00 PM (Noon)                ✓    │
│ 1:00 PM                             │
│ ...                                 │
│ 11:00 PM                            │
└─────────────────────────────────────┘
```

### Month Dropdown:
```
Month
┌─────────────────────────────────────┐
│ June                            ▼  │
└─────────────────────────────────────┘
        ↓
┌─────────────────────────────────────┐
│ January                             │
│ February                            │
│ March                               │
│ April                               │
│ May                                 │
│ June                           ✓    │
│ July                                │
│ August                              │
│ September                           │
│ October                             │
│ November                            │
│ December                            │
└─────────────────────────────────────┘
```

✓ All options visible
✓ Current selection marked
✓ Easy to click

---

## 7. Hovering Over Button

### Normal State:
```
┌─────────────────────────────────────┐
│   Predict Solar Irradiance          │ ← Blue (#0071e3)
└─────────────────────────────────────┘
```

### Hover State:
```
┌─────────────────────────────────────┐
│   Predict Solar Irradiance          │ ← Slightly brighter blue
└─────────────────────────────────────┘
  ↑
  Color: #0077ED
  Slight scale effect (1.01)
  Cursor: pointer
```

✓ Button responds to hover
✓ Smooth transition

---

## 8. Clicking Submit Button

### During Prediction:
```
┌─────────────────────────────────────┐
│   Predicting...                     │ ← Text changes
└─────────────────────────────────────┘
  ↑
  Button disabled
  Opacity: 0.6
  Cannot click again
```

✓ Button shows loading state
✓ Prevents double-submission

---

## 9. Successful Prediction Result

### What You Should See:
```
┌─────────────────────────────────────┐
│   Predict Solar Irradiance          │ ← Button back to normal
└─────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ PREDICTED SOLAR IRRADIANCE                  │ ← Small gray label
│                                             │
│ 428.21 W/m²                                 │ ← Large number (56px)
│                                             │
│ Good solar irradiance. Mostly clear sky     │ ← Interpretation
│ with strong solar energy generation         │
│ potential.                                  │
└─────────────────────────────────────────────┘
  ↑
  Gray background (#f5f5f7)
  Rounded corners
  Generous padding
```

✓ Result appears below form
✓ Large, easy-to-read number
✓ Helpful interpretation text

---

## 10. Different Result Scenarios

### Scenario A: High Irradiance (>600 W/m²)
```
┌─────────────────────────────────────────────┐
│ PREDICTED SOLAR IRRADIANCE                  │
│                                             │
│ 650.45 W/m²                                 │
│                                             │
│ Excellent solar irradiance. Clear sky       │
│ conditions with optimal solar energy        │
│ generation.                                 │
└─────────────────────────────────────────────┘
```

### Scenario B: Moderate Irradiance (300-600 W/m²)
```
┌─────────────────────────────────────────────┐
│ PREDICTED SOLAR IRRADIANCE                  │
│                                             │
│ 428.21 W/m²                                 │
│                                             │
│ Moderate solar irradiance. Partly cloudy    │
│ conditions with reasonable solar energy     │
│ potential.                                  │
└─────────────────────────────────────────────┘
```

### Scenario C: Low Irradiance (100-300 W/m²)
```
┌─────────────────────────────────────────────┐
│ PREDICTED SOLAR IRRADIANCE                  │
│                                             │
│ 156.78 W/m²                                 │
│                                             │
│ Low solar irradiance. Cloudy conditions     │
│ are significantly reducing solar energy     │
│ availability.                               │
└─────────────────────────────────────────────┘
```

### Scenario D: Very Low Irradiance (<100 W/m²)
```
┌─────────────────────────────────────────────┐
│ PREDICTED SOLAR IRRADIANCE                  │
│                                             │
│ 45.32 W/m²                                  │
│                                             │
│ Very low solar irradiance. Conditions are   │
│ heavily overcast or it's early morning/late │
│ evening.                                    │
└─────────────────────────────────────────────┘
```

### Scenario E: Night Time (0 W/m²)
```
┌─────────────────────────────────────────────┐
│ PREDICTED SOLAR IRRADIANCE                  │
│                                             │
│ 0.0 W/m²                                    │
│                                             │
│ No solar irradiance detected. This is       │
│ typical for nighttime or very low light     │
│ conditions.                                 │
└─────────────────────────────────────────────┘
```

✓ Interpretation matches the value
✓ Clear explanation for each range

---

## 11. Error Scenario (API Offline)

### What You Should See:
```
┌─────────────────────────────────────┐
│   Predict Solar Irradiance          │
└─────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ Error: Unable to connect to prediction      │ ← Red background
│ service. Make sure the Flask API is running │
│ at http://localhost:5000                    │
└─────────────────────────────────────────────┘
  ↑
  Red/pink background (#fff3f3)
  Red border (#ffcccc)
  Red text (#d32f2f)
```

✓ Clear error message
✓ Tells you what to do
✓ Red color indicates error

---

## 12. Mobile View (375px width)

### What You Should See:
```
┌───────────────────────────┐
│ Profile | Data | Analysis │ ← Navigation wraps
│ Insights | Prediction |   │
│ Summary                   │
├───────────────────────────┤
│                           │
│    Prediction             │
│                           │
│ ┌───────────────────────┐ │
│ │ Solar Irradiance      │ │
│ │ Prediction            │ │
│ │                       │ │
│ │ Temperature           │ │
│ │ ┌───────────────────┐ │ │
│ │ │ 30            °C  │ │ │
│ │ └───────────────────┘ │ │
│ │                       │ │
│ │ [All fields stack]    │ │
│ │                       │ │
│ │ ┌───────────────────┐ │ │
│ │ │ Predict           │ │ │
│ │ └───────────────────┘ │ │
│ └───────────────────────┘ │
└───────────────────────────┘
```

✓ Form adapts to small screen
✓ All fields remain usable
✓ No horizontal scrolling
✓ Text remains readable

---

## 13. Browser Console (F12) - No Errors

### What You Should See:
```
Console
  ▼ index.html:1
  ▼ script.js:1
  
  [No errors]
```

✓ No red error messages
✓ No warnings (or only harmless ones)
✓ Clean console

---

## 14. Network Tab (F12) - Successful Request

### What You Should See:
```
Network
Name                Method  Status  Type    Size    Time
predict             POST    200     xhr     245B    234ms
```

✓ Status: 200 (success)
✓ Response time: <1 second
✓ Type: xhr (AJAX request)

### Request Payload:
```json
{
  "temperature": 25,
  "cloud_cover": 30,
  "humidity": 60,
  "hour": 12,
  "month": 6
}
```

### Response:
```json
{
  "predicted_solar_irradiance": 402.87,
  "status": "success",
  "unit": "W/m²",
  "input_features": {
    "temperature": 25.0,
    "cloud_cover": 30.0,
    "humidity": 60.0,
    "hour": 12,
    "month": 6
  }
}
```

✓ Clean request/response
✓ All data correct

---

## Summary Checklist

When testing, you should see:

VISUAL:
- [ ] Clean Apple-style design
- [ ] Centered form (max 800px)
- [ ] White card with shadow
- [ ] Blue button (#0071e3)
- [ ] Clear labels and units

INTERACTIVE:
- [ ] Blue glow on focus
- [ ] Hover effects on button
- [ ] Dropdowns open smoothly
- [ ] Loading state during prediction

FUNCTIONAL:
- [ ] Predictions appear in <1 second
- [ ] Large result display (56px)
- [ ] Helpful interpretation text
- [ ] Error messages when API offline

RESULTS:
- [ ] Sunny day: >400 W/m²
- [ ] Cloudy day: <100 W/m²
- [ ] Night time: 0 W/m²
- [ ] Noon: High values
- [ ] Morning/Evening: Low values

If you see all of these, your system is perfect! ✓
