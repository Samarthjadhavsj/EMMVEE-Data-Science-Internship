# Browser Testing Checklist

## Setup
- [ ] Flask API is running: `python app.py`
- [ ] Open `index.html` in browser
- [ ] Click "Prediction" in navigation

---

## Visual Inspection

### Form Layout
- [ ] Form is centered on page
- [ ] Maximum width is 800px
- [ ] White background with subtle shadow
- [ ] Title "Solar Irradiance Prediction" is large (40px)
- [ ] Subtitle text is gray and centered

### Input Fields
- [ ] Temperature field shows "°C" unit on right
- [ ] Cloud Cover field shows "%" unit on right
- [ ] All fields have light gray background (#f5f5f7)
- [ ] Labels are small and gray (14px)
- [ ] Input text is readable (17px)

### Dropdowns
- [ ] Humidity dropdown shows 8 options
- [ ] Hour dropdown shows 24 options in AM/PM format
- [ ] Month dropdown shows full month names
- [ ] Dropdown arrow icon is visible
- [ ] Selected value is clearly displayed

### Button
- [ ] Button is full width
- [ ] Blue color (#0071e3)
- [ ] Text is white and centered
- [ ] Rounded corners (12px)
- [ ] Text says "Predict Solar Irradiance"

---

## Interactive Testing

### Focus Effects
- [ ] Click temperature input → Blue glow appears
- [ ] Click cloud cover input → Blue glow appears
- [ ] Click any dropdown → Blue glow appears
- [ ] Click outside → Glow disappears

### Hover Effects
- [ ] Hover over button → Color changes slightly
- [ ] Hover over button → Slight scale effect
- [ ] Cursor changes to pointer on button

### Form Submission
- [ ] Click button → Text changes to "Predicting..."
- [ ] Button becomes disabled during prediction
- [ ] Button opacity reduces during prediction
- [ ] After response → Button returns to normal

---

## Functional Testing

### Test Case 1: Default Values
**Input:**
- Temperature: 25°C
- Cloud Cover: 30%
- Humidity: Moderate-High (60%)
- Time: 12:00 PM
- Month: June

**Expected:**
- [ ] Prediction appears in ~1 second
- [ ] Result shows ~400 W/m²
- [ ] Large number display (56px)
- [ ] Interpretation text appears
- [ ] Gray background box for result

### Test Case 2: Sunny Day
**Input:**
- Temperature: 35°C
- Cloud Cover: 10%
- Humidity: Very Low (20%)
- Time: 1:00 PM
- Month: May

**Expected:**
- [ ] High irradiance (>400 W/m²)
- [ ] Interpretation: "Excellent" or "Good"

### Test Case 3: Cloudy Day
**Input:**
- Temperature: 22°C
- Cloud Cover: 85%
- Humidity: Very High (80%)
- Time: 2:00 PM
- Month: July

**Expected:**
- [ ] Low irradiance (<100 W/m²)
- [ ] Interpretation mentions cloudy conditions

### Test Case 4: Night Time
**Input:**
- Temperature: 18°C
- Cloud Cover: 50%
- Humidity: Moderate (50%)
- Time: 12:00 AM (Midnight)
- Month: Any

**Expected:**
- [ ] Result shows 0 W/m²
- [ ] Interpretation mentions nighttime

### Test Case 5: Early Morning
**Input:**
- Temperature: 16°C
- Cloud Cover: 40%
- Humidity: High (70%)
- Time: 6:00 AM
- Month: March

**Expected:**
- [ ] Very low or zero irradiance
- [ ] Interpretation appropriate for morning

### Test Case 6: Late Evening
**Input:**
- Temperature: 20°C
- Cloud Cover: 30%
- Humidity: Moderate-High (60%)
- Time: 6:00 PM
- Month: September

**Expected:**
- [ ] Very low or zero irradiance
- [ ] Interpretation appropriate for evening

---

## Dropdown Testing

### Humidity Dropdown
Test each option:
- [ ] Very Low (20%)
- [ ] Low (30%)
- [ ] Moderate-Low (40%)
- [ ] Moderate (50%)
- [ ] Moderate-High (60%)
- [ ] High (70%)
- [ ] Very High (80%)
- [ ] Extremely High (90%)

**Expected:** All values work, predictions vary slightly

### Hour Dropdown (Sample)
Test key hours:
- [ ] 12:00 AM (Midnight) → 0 W/m²
- [ ] 6:00 AM → Low/zero
- [ ] 12:00 PM (Noon) → High irradiance
- [ ] 1:00 PM → High irradiance
- [ ] 6:00 PM → Low/zero
- [ ] 11:00 PM → 0 W/m²

### Month Dropdown
Test seasonal variation:
- [ ] January (Winter) → Moderate
- [ ] April (Spring) → Moderate-High
- [ ] July (Summer) → High
- [ ] October (Fall) → Moderate-High

---

## Error Handling

### API Offline Test
1. [ ] Stop Flask API (Ctrl+C in terminal)
2. [ ] Try to submit form
3. [ ] Red error box appears
4. [ ] Error message mentions connection issue
5. [ ] Error message is clear and helpful

### Recovery Test
1. [ ] Restart Flask API
2. [ ] Submit form again
3. [ ] Prediction works normally

---

## Result Display Testing

### Result Box
- [ ] Appears below form after prediction
- [ ] Light gray background (#f5f5f7)
- [ ] Rounded corners (18px)
- [ ] Generous padding (32px)

### Result Content
- [ ] Small gray label "PREDICTED SOLAR IRRADIANCE"
- [ ] Large number (56px, bold)
- [ ] Unit "W/m²" is included
- [ ] Interpretation text below
- [ ] Interpretation is relevant to value

### Interpretation Accuracy
- [ ] 0 W/m² → Mentions nighttime
- [ ] <100 W/m² → Mentions very low/cloudy
- [ ] 100-300 W/m² → Mentions low/cloudy
- [ ] 300-600 W/m² → Mentions moderate/partly cloudy
- [ ] 600-800 W/m² → Mentions good conditions
- [ ] >800 W/m² → Mentions excellent conditions

---

## Cross-Browser Testing

### Chrome
- [ ] Form displays correctly
- [ ] Dropdowns work
- [ ] Predictions work
- [ ] No console errors (F12)

### Firefox
- [ ] Form displays correctly
- [ ] Dropdowns work
- [ ] Predictions work
- [ ] No console errors (F12)

### Edge
- [ ] Form displays correctly
- [ ] Dropdowns work
- [ ] Predictions work
- [ ] No console errors (F12)

---

## Mobile Responsiveness

### Open DevTools (F12) → Device Toolbar

#### iPhone SE (375px)
- [ ] Form is readable
- [ ] Inputs are usable
- [ ] Button is tappable
- [ ] No horizontal scroll

#### iPad (768px)
- [ ] Form looks good
- [ ] Proper spacing
- [ ] Easy to use

#### Desktop (1920px)
- [ ] Form is centered
- [ ] Max-width 800px maintained
- [ ] Looks professional

---

## Accessibility Testing

### Keyboard Navigation
- [ ] Tab through all fields in order
- [ ] Tab reaches button
- [ ] Enter key submits form
- [ ] Dropdowns open with keyboard
- [ ] Arrow keys work in dropdowns

### Screen Reader (Optional)
- [ ] Labels are announced
- [ ] Input values are announced
- [ ] Button purpose is clear

---

## Performance Testing

### Response Time
- [ ] Prediction completes in <2 seconds
- [ ] No lag when typing
- [ ] Smooth animations

### Multiple Predictions
- [ ] Submit 5 predictions in a row
- [ ] All work correctly
- [ ] No slowdown

---

## Edge Cases

### Boundary Values
- [ ] Temperature: -10°C (minimum)
- [ ] Temperature: 50°C (maximum)
- [ ] Cloud Cover: 0% (clear sky)
- [ ] Cloud Cover: 100% (overcast)

### Rapid Clicking
- [ ] Click button multiple times quickly
- [ ] Only one request is processed
- [ ] No errors occur

---

## Final Checks

### Overall Experience
- [ ] Form looks professional
- [ ] Matches Apple design aesthetic
- [ ] Easy to understand
- [ ] Easy to use
- [ ] Results are clear
- [ ] No confusing elements

### Documentation
- [ ] User knows what each field means
- [ ] Units are clearly shown
- [ ] Results are interpretable

---

## Sign-Off

**Tester Name:** ___________________

**Date:** ___________________

**Browser:** ___________________

**Result:** 
- [ ] All tests passed - Ready for production
- [ ] Minor issues found (list below)
- [ ] Major issues found (list below)

**Issues Found:**
_________________________________
_________________________________
_________________________________

**Additional Notes:**
_________________________________
_________________________________
_________________________________
