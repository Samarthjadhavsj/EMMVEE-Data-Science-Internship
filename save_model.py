"""
================================================================================
SAVE TRAINED MODEL AND SCALER
================================================================================
Project: Intelligent Solar Energy Analytics & Prediction System
Role: Machine Learning Engineer
Organization: Emmvee Solar Systems Pvt. Ltd.

Purpose: Save trained Random Forest model and scaler for deployment
================================================================================
"""

import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

print("="*80)
print("SAVING TRAINED MODEL AND SCALER")
print("="*80)
print()

# Load training data
print("Loading training data...")
X_train = pd.read_csv('X_train_scaled.csv')
y_train = pd.read_csv('y_train.csv')['solar_irradiance']

# Load original unscaled data to fit scaler
X_train_original = pd.read_csv('weather_environmental_data.csv')
feature_columns = ['temperature', 'cloud_cover', 'humidity', 'hour', 'month']
X_train_original = X_train_original[feature_columns].dropna()

print("✓ Data loaded")
print()

# Train and save scaler
print("Fitting and saving StandardScaler...")
scaler = StandardScaler()
scaler.fit(X_train_original)
joblib.dump(scaler, 'scaler.pkl')
print("✓ Scaler saved: scaler.pkl")
print()

# Train and save model
print("Training and saving Random Forest model...")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
joblib.dump(model, 'random_forest_model.pkl')
print("✓ Model saved: random_forest_model.pkl")
print()

print("="*80)
print("MODEL AND SCALER SAVED SUCCESSFULLY")
print("="*80)
print()
print("Files created:")
print("  - random_forest_model.pkl")
print("  - scaler.pkl")
print()
print("Ready for Flask deployment!")
print("="*80)
