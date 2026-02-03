"""
================================================================================
BASELINE MODEL TRAINING - SOLAR IRRADIANCE PREDICTION
================================================================================
Project: Intelligent Solar Energy Analytics & Prediction System
Role: Data Scientist
Organization: Emmvee Solar Systems Pvt. Ltd.

Purpose: Train and evaluate baseline regression models
Phase: Prediction - Model Training and Evaluation
================================================================================
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

print("="*80)
print("BASELINE MODEL TRAINING - SOLAR IRRADIANCE PREDICTION")
print("="*80)
print()

# ============================================================================
# STEP 1: LOAD PREPARED DATASETS
# ============================================================================

print("STEP 1: Loading prepared datasets...")

X_train = pd.read_csv('X_train_scaled.csv')
X_test = pd.read_csv('X_test_scaled.csv')
y_train = pd.read_csv('y_train.csv')['solar_irradiance']
y_test = pd.read_csv('y_test.csv')['solar_irradiance']

print(f"✓ Training set: {X_train.shape[0]} samples, {X_train.shape[1]} features")
print(f"✓ Testing set:  {X_test.shape[0]} samples, {X_test.shape[1]} features")
print()

# ============================================================================
# STEP 2: MODEL 1 - LINEAR REGRESSION
# ============================================================================

print("="*80)
print("MODEL 1: LINEAR REGRESSION")
print("="*80)
print()

print("Model Description:")
print("  Linear Regression serves as a baseline model that assumes a linear")
print("  relationship between input features and solar irradiance. It provides")
print("  a simple reference point for comparing more complex models.")
print()

print("Training Linear Regression model...")
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
print("✓ Model trained")
print()

# Make predictions
lr_train_pred = lr_model.predict(X_train)
lr_test_pred = lr_model.predict(X_test)

# Calculate metrics
lr_train_mae = mean_absolute_error(y_train, lr_train_pred)
lr_train_rmse = np.sqrt(mean_squared_error(y_train, lr_train_pred))
lr_train_r2 = r2_score(y_train, lr_train_pred)

lr_test_mae = mean_absolute_error(y_test, lr_test_pred)
lr_test_rmse = np.sqrt(mean_squared_error(y_test, lr_test_pred))
lr_test_r2 = r2_score(y_test, lr_test_pred)

print("Training Set Performance:")
print(f"  MAE:  {lr_train_mae:.2f} W/m²")
print(f"  RMSE: {lr_train_rmse:.2f} W/m²")
print(f"  R²:   {lr_train_r2:.4f}")
print()

print("Testing Set Performance:")
print(f"  MAE:  {lr_test_mae:.2f} W/m²")
print(f"  RMSE: {lr_test_rmse:.2f} W/m²")
print(f"  R²:   {lr_test_r2:.4f}")
print()

# ============================================================================
# STEP 3: MODEL 2 - DECISION TREE REGRESSOR
# ============================================================================

print("="*80)
print("MODEL 2: DECISION TREE REGRESSOR")
print("="*80)
print()

print("Model Description:")
print("  Decision Tree Regressor can capture non-linear relationships and")
print("  interactions between features. It creates a tree-like structure of")
print("  decision rules to predict solar irradiance based on feature values.")
print()

print("Training Decision Tree Regressor model...")
dt_model = DecisionTreeRegressor(random_state=42)
dt_model.fit(X_train, y_train)
print("✓ Model trained")
print()

# Make predictions
dt_train_pred = dt_model.predict(X_train)
dt_test_pred = dt_model.predict(X_test)

# Calculate metrics
dt_train_mae = mean_absolute_error(y_train, dt_train_pred)
dt_train_rmse = np.sqrt(mean_squared_error(y_train, dt_train_pred))
dt_train_r2 = r2_score(y_train, dt_train_pred)

dt_test_mae = mean_absolute_error(y_test, dt_test_pred)
dt_test_rmse = np.sqrt(mean_squared_error(y_test, dt_test_pred))
dt_test_r2 = r2_score(y_test, dt_test_pred)

print("Training Set Performance:")
print(f"  MAE:  {dt_train_mae:.2f} W/m²")
print(f"  RMSE: {dt_train_rmse:.2f} W/m²")
print(f"  R²:   {dt_train_r2:.4f}")
print()

print("Testing Set Performance:")
print(f"  MAE:  {dt_test_mae:.2f} W/m²")
print(f"  RMSE: {dt_test_rmse:.2f} W/m²")
print(f"  R²:   {dt_test_r2:.4f}")
print()

# ============================================================================
# STEP 4: MODEL 3 - RANDOM FOREST REGRESSOR
# ============================================================================

print("="*80)
print("MODEL 3: RANDOM FOREST REGRESSOR")
print("="*80)
print()

print("Model Description:")
print("  Random Forest is an ensemble model that combines multiple decision trees")
print("  to improve prediction accuracy and reduce overfitting. It averages")
print("  predictions from many trees, making it robust for solar irradiance")
print("  prediction where relationships can be complex and non-linear.")
print()

print("Training Random Forest Regressor model...")
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
print("✓ Model trained with 100 trees")
print()

# Make predictions
rf_train_pred = rf_model.predict(X_train)
rf_test_pred = rf_model.predict(X_test)

# Calculate metrics
rf_train_mae = mean_absolute_error(y_train, rf_train_pred)
rf_train_rmse = np.sqrt(mean_squared_error(y_train, rf_train_pred))
rf_train_r2 = r2_score(y_train, rf_train_pred)

rf_test_mae = mean_absolute_error(y_test, rf_test_pred)
rf_test_rmse = np.sqrt(mean_squared_error(y_test, rf_test_pred))
rf_test_r2 = r2_score(y_test, rf_test_pred)

print("Training Set Performance:")
print(f"  MAE:  {rf_train_mae:.2f} W/m²")
print(f"  RMSE: {rf_train_rmse:.2f} W/m²")
print(f"  R²:   {rf_train_r2:.4f}")
print()

print("Testing Set Performance:")
print(f"  MAE:  {rf_test_mae:.2f} W/m²")
print(f"  RMSE: {rf_test_rmse:.2f} W/m²")
print(f"  R²:   {rf_test_r2:.4f}")
print()

# ============================================================================
# STEP 5: MODEL COMPARISON
# ============================================================================

print("="*80)
print("MODEL COMPARISON - TESTING SET PERFORMANCE")
print("="*80)
print()

# Create comparison table
comparison_data = {
    'Model': ['Linear Regression', 'Decision Tree', 'Random Forest'],
    'MAE (W/m²)': [lr_test_mae, dt_test_mae, rf_test_mae],
    'RMSE (W/m²)': [lr_test_rmse, dt_test_rmse, rf_test_rmse],
    'R² Score': [lr_test_r2, dt_test_r2, rf_test_r2]
}

comparison_df = pd.DataFrame(comparison_data)
print(comparison_df.to_string(index=False))
print()

# Identify best model
best_model_idx = comparison_df['R² Score'].idxmax()
best_model_name = comparison_df.loc[best_model_idx, 'Model']

print("="*80)
print("PERFORMANCE ANALYSIS")
print("="*80)
print()

print(f"Best Performing Model: {best_model_name}")
print(f"  - Highest R² Score: {comparison_df.loc[best_model_idx, 'R² Score']:.4f}")
print(f"  - Lowest MAE: {comparison_df.loc[best_model_idx, 'MAE (W/m²)']:.2f} W/m²")
print(f"  - Lowest RMSE: {comparison_df.loc[best_model_idx, 'RMSE (W/m²)']:.2f} W/m²")
print()

print("Model Behavior Observations:")
print("-"*80)

if lr_test_r2 < dt_test_r2 and lr_test_r2 < rf_test_r2:
    print("• Linear Regression shows lower performance, indicating non-linear")
    print("  relationships between features and solar irradiance")
    print()

if dt_train_r2 > dt_test_r2 + 0.1:
    print("• Decision Tree shows signs of overfitting with higher training")
    print("  performance compared to testing performance")
    print()

if rf_test_r2 > lr_test_r2 and rf_test_r2 > dt_test_r2:
    print("• Random Forest achieves best performance by combining multiple trees,")
    print("  effectively capturing complex patterns while reducing overfitting")
    print()

print("="*80)
print("BASELINE MODEL TRAINING COMPLETE")
print("="*80)
print()

print("Summary:")
print("  ✓ Three baseline models trained successfully")
print("  ✓ All models evaluated on testing set")
print("  ✓ Performance metrics calculated and compared")
print("  ✓ Models ready for further analysis")
print()

print("Next Steps:")
print("  - Analyze feature importance")
print("  - Consider hyperparameter tuning for best model")
print("  - Evaluate model predictions visually")
print()

print("="*80)
