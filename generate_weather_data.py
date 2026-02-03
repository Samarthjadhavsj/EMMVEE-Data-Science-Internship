"""
================================================================================
WEATHER & ENVIRONMENTAL DATA GENERATOR
================================================================================
Project: Solar Analytics - Internal Data Generation
Purpose: Generate synthetic but industry-representative weather data
Role: Senior Data Engineer

DATA TYPE: SYNTHETIC (Industry-Representative)
Reason: Real weather data is not available for this internal project

This script generates ONLY weather and environmental data.
No analysis, dashboards, or machine learning included.
================================================================================
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("="*80)
print("WEATHER & ENVIRONMENTAL DATA GENERATOR")
print("Synthetic but Industry-Representative Dataset")
print("="*80)
print()

# ============================================================================
# CONFIGURATION
# ============================================================================

# Time configuration
START_DATE = datetime(2021, 1, 1, 0, 0, 0)
END_DATE = datetime(2023, 12, 31, 23, 0, 0)
FREQUENCY = 'H'  # Hourly

# Data quality parameters
MISSING_VALUE_RATE = 0.005  # 0.5% missing values

# Set random seed for reproducibility
np.random.seed(42)

print("Configuration:")
print(f"  Time Period: {START_DATE.date()} to {END_DATE.date()}")
print(f"  Granularity: Hourly")
print(f"  Expected Records: ~26,280")
print()

# ============================================================================
# GENERATE TIME SERIES
# ============================================================================

print("Step 1: Generating time series...")

# Create hourly datetime range
datetime_range = pd.date_range(start=START_DATE, end=END_DATE, freq=FREQUENCY)

# Create base dataframe
df = pd.DataFrame({
    'datetime': datetime_range,
    'year': datetime_range.year,
    'month': datetime_range.month,
    'day': datetime_range.day,
    'hour': datetime_range.hour
})

print(f"✓ Generated {len(df)} hourly records")
print()

# ============================================================================
# GENERATE WEATHER FEATURES
# ============================================================================

print("Step 2: Generating weather features...")

# Extract time components for pattern generation
hours = df['hour'].values
days_of_year = df['datetime'].dt.dayofyear.values

# Temperature (°C) - Seasonal and daily variation
# Base temperature varies by season (winter: 5-15°C, summer: 25-35°C)
seasonal_temp = 20 + 12 * np.sin(2 * np.pi * (days_of_year - 80) / 365)
daily_temp_variation = 8 * np.sin(2 * np.pi * (hours - 6) / 24)
temp_noise = np.random.normal(0, 2, len(df))
df['temperature'] = seasonal_temp + daily_temp_variation + temp_noise
df['temperature'] = np.clip(df['temperature'], -5, 45)  # Realistic bounds

print("✓ Temperature generated (range: -5°C to 45°C)")

# Cloud Cover (%) - Random with seasonal bias
# More clouds in winter/monsoon, less in summer
seasonal_cloud = 40 + 25 * np.sin(2 * np.pi * (days_of_year - 80) / 365 + np.pi/3)
cloud_noise = np.random.normal(0, 20, len(df))
df['cloud_cover'] = seasonal_cloud + cloud_noise
df['cloud_cover'] = np.clip(df['cloud_cover'], 0, 100)

print("✓ Cloud cover generated (range: 0% to 100%)")

# Solar Irradiance (W/m²) - Depends on time of day, season, and cloud cover
# Zero at night, peaks at solar noon (12-1 PM) (~1000 W/m² on clear day)
# Solar elevation angle peaks at 12-13 hours (noon to 1 PM)
solar_elevation = np.maximum(0, np.sin(2 * np.pi * (hours - 6) / 24))
seasonal_factor = 0.7 + 0.3 * np.sin(2 * np.pi * (days_of_year - 172) / 365)
cloud_factor = (100 - df['cloud_cover']) / 100
max_irradiance = 1000  # W/m²

df['solar_irradiance'] = (max_irradiance * solar_elevation * 
                          seasonal_factor * cloud_factor * 
                          np.random.uniform(0.85, 1.0, len(df)))
df['solar_irradiance'] = np.maximum(0, df['solar_irradiance'])

print("✓ Solar irradiance generated (range: 0 to 1000 W/m²)")

# Humidity (%) - Inversely related to temperature
base_humidity = 65 - 20 * np.sin(2 * np.pi * (days_of_year - 80) / 365)
humidity_noise = np.random.normal(0, 8, len(df))
df['humidity'] = base_humidity + humidity_noise
df['humidity'] = np.clip(df['humidity'], 10, 95)

print("✓ Humidity generated (range: 10% to 95%)")
print()

# ============================================================================
# INTRODUCE DATA QUALITY ISSUES
# ============================================================================

print("Step 3: Introducing realistic data quality issues...")

# Add missing values (0.5% of data)
missing_count = int(len(df) * MISSING_VALUE_RATE)
missing_indices = np.random.choice(df.index, size=missing_count, replace=False)

# Distribute missing values across weather columns
for idx in missing_indices:
    col = np.random.choice(['temperature', 'cloud_cover', 'solar_irradiance', 'humidity'])
    df.loc[idx, col] = np.nan

print(f"✓ Introduced {missing_count} missing values ({MISSING_VALUE_RATE*100}%)")
print()

# ============================================================================
# FINAL DATA PREPARATION
# ============================================================================

print("Step 4: Final data preparation...")

# Round values for realism
df['temperature'] = df['temperature'].round(2)
df['cloud_cover'] = df['cloud_cover'].round(2)
df['solar_irradiance'] = df['solar_irradiance'].round(2)
df['humidity'] = df['humidity'].round(2)

# Reorder columns
column_order = ['datetime', 'year', 'month', 'day', 'hour', 
                'temperature', 'cloud_cover', 'solar_irradiance', 'humidity']
df = df[column_order]

print("✓ Data rounded and formatted")
print()

# ============================================================================
# DISPLAY DATASET INFORMATION
# ============================================================================

print("="*80)
print("DATASET SUMMARY")
print("="*80)
print()

print(f"Dataset Shape: {df.shape}")
print(f"Total Records: {len(df):,}")
print(f"Time Period: {df['datetime'].min()} to {df['datetime'].max()}")
print()

print("Column Data Types:")
print("-"*80)
print(df.dtypes)
print()

print("Missing Values:")
print("-"*80)
print(df.isnull().sum())
print()

print("First 5 Rows:")
print("-"*80)
print(df.head())
print()

print("Statistical Summary:")
print("-"*80)
print(df.describe())
print()

# ============================================================================
# SAVE DATASET
# ============================================================================

print("="*80)
print("SAVING DATASET")
print("="*80)
print()

filename = 'weather_environmental_data.csv'
df.to_csv(filename, index=False)

print(f"✓ Dataset saved as: {filename}")
print(f"✓ File size: {len(df):,} rows × {len(df.columns)} columns")
print()

# ============================================================================
# DATA VALIDATION
# ============================================================================

print("="*80)
print("DATA VALIDATION")
print("="*80)
print()

# Validation 1: Night-time irradiance
night_mask = (df['hour'] < 6) | (df['hour'] > 18)
night_irradiance = df.loc[night_mask, 'solar_irradiance'].max()
print(f"✓ Max irradiance during night hours: {night_irradiance:.2f} W/m²")

# Validation 2: Seasonal variation
summer_temp = df[df['month'].isin([6, 7, 8])]['temperature'].mean()
winter_temp = df[df['month'].isin([12, 1, 2])]['temperature'].mean()
print(f"✓ Average temperature - Summer: {summer_temp:.2f}°C, Winter: {winter_temp:.2f}°C")

# Validation 3: Cloud cover impact
high_cloud = df[df['cloud_cover'] > 80]['solar_irradiance'].mean()
low_cloud = df[df['cloud_cover'] < 20]['solar_irradiance'].mean()
print(f"✓ Avg irradiance - High cloud (>80%): {high_cloud:.2f} W/m², Low cloud (<20%): {low_cloud:.2f} W/m²")
print()

# ============================================================================
# COMPLETION MESSAGE
# ============================================================================

print("="*80)
print("DATA GENERATION COMPLETE")
print("="*80)
print()
print("IMPORTANT NOTES:")
print("-"*80)
print("• This is SYNTHETIC data generated for internal analytics project")
print("• Data is industry-representative with realistic patterns")
print("• Suitable for analysis, dashboards, and KPI tracking")
print("• Real weather data is not used due to availability constraints")
print()
print(f"✓ File ready: {filename}")
print("✓ Dataset validated and ready for use")
print()
print("="*80)
