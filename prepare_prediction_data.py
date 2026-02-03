"""
================================================================================
DATA PREPARATION FOR PREDICTION
================================================================================
Project: Intelligent Solar Energy Analytics & Prediction System
Role: Data Scientist
Organization: Emmvee Solar Systems Pvt. Ltd.

Purpose: Prepare dataset for predictive modeling
Phase: Prediction - Data Preparation Only
================================================================================
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

print("="*80)
print("DATA PREPARATION FOR PREDICTION")
print("="*80)
print()

# ============================================================================
# STEP 1: LOAD DATASET
# ============================================================================

print("STEP 1: Loading dataset...")
df = pd.read_csv('weather_environmental_data.csv')
print(f"✓ Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print()

# ============================================================================
# STEP 2: FEATURE SELECTION
# ============================================================================

print("STEP 2: Selecting features and target variable...")

# Input features (X)
feature_columns = ['temperature', 'cloud_cover', 'humidity', 'hour', 'month']
X = df[feature_columns].copy()

# Target variable (y)
y = df['solar_irradiance'].copy()

print("Input Features (X):")
for i, col in enumerate(feature_columns, 1):
    print(f"  {i}. {col}")
print()
print("Target Variable (y):")
print("  - solar_irradiance")
print()

# ============================================================================
# STEP 3: MISSING VALUE HANDLING
# ============================================================================

print("STEP 3: Handling missing values...")

# Check for missing values
missing_before = X.isnull().sum()
print("Missing values in features:")
print(missing_before)
print()

missing_target = y.isnull().sum()
print(f"Missing values in target: {missing_target}")
print()

# Handle missing values by removing rows with any missing data
# This ensures clean data for modeling
initial_rows = len(X)
mask = ~(X.isnull().any(axis=1) | y.isnull())
X = X[mask]
y = y[mask]
rows_removed = initial_rows - len(X)

print(f"Method: Row removal")
print(f"✓ Removed {rows_removed} rows with missing values")
print(f"✓ Clean dataset: {len(X)} rows")
print()

# ============================================================================
# STEP 4: TRAIN-TEST SPLIT
# ============================================================================

print("STEP 4: Splitting data into training and testing sets...")

# Split ratio: 80% training, 20% testing
# random_state=42 ensures reproducibility
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42
)

print("Split Configuration:")
print("  - Training set: 80%")
print("  - Testing set: 20%")
print("  - Random state: 42 (for reproducibility)")
print()

print("Dataset Shapes:")
print(f"  X_train: {X_train.shape}")
print(f"  X_test:  {X_test.shape}")
print(f"  y_train: {y_train.shape}")
print(f"  y_test:  {y_test.shape}")
print()

# ============================================================================
# STEP 5: FEATURE SCALING
# ============================================================================

print("STEP 5: Applying feature scaling...")

# Initialize StandardScaler
scaler = StandardScaler()

# Fit scaler on training data and transform both train and test
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Convert back to DataFrame for better readability
X_train_scaled = pd.DataFrame(X_train_scaled, columns=feature_columns, index=X_train.index)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=feature_columns, index=X_test.index)

print("Method: StandardScaler (Z-score normalization)")
print("Reason: Features have different scales (e.g., temperature: 0-40°C, cloud_cover: 0-100%)")
print("        Scaling ensures all features contribute equally to model training")
print()

print("✓ Training features scaled")
print("✓ Testing features scaled")
print()

# ============================================================================
# STEP 6: OUTPUT VALIDATION
# ============================================================================

print("="*80)
print("DATA PREPARATION COMPLETE")
print("="*80)
print()

print("Final Dataset Summary:")
print("-"*80)
print(f"Training samples: {len(X_train_scaled)}")
print(f"Testing samples:  {len(X_test_scaled)}")
print(f"Total samples:    {len(X_train_scaled) + len(X_test_scaled)}")
print()

print("Feature Statistics (Training Set - Scaled):")
print("-"*80)
print(X_train_scaled.describe())
print()

print("Target Variable Statistics (Training Set):")
print("-"*80)
print(y_train.describe())
print()

print("Data Preparation Status:")
print("-"*80)
print("✓ Features selected and separated")
print("✓ Target variable identified")
print("✓ Missing values handled")
print("✓ Train-test split completed")
print("✓ Feature scaling applied")
print("✓ Data is model-ready")
print()

# ============================================================================
# SAVE PREPARED DATA (OPTIONAL)
# ============================================================================

print("Saving prepared datasets...")

# Save to CSV for future use
X_train_scaled.to_csv('X_train_scaled.csv', index=False)
X_test_scaled.to_csv('X_test_scaled.csv', index=False)
y_train.to_csv('y_train.csv', index=False, header=['solar_irradiance'])
y_test.to_csv('y_test.csv', index=False, header=['solar_irradiance'])

print("✓ X_train_scaled.csv")
print("✓ X_test_scaled.csv")
print("✓ y_train.csv")
print("✓ y_test.csv")
print()

print("="*80)
print("READY FOR MODEL TRAINING")
print("="*80)
print()
print("Next Steps:")
print("  1. Select appropriate regression algorithm")
print("  2. Train model on training data")
print("  3. Evaluate model performance on testing data")
print()
print("="*80)
