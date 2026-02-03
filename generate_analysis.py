"""
================================================================================
COMPREHENSIVE ANALYSIS - SOLAR ENERGY ANALYTICS
================================================================================
Project: Intelligent Solar Energy Analytics & Prediction System
Role: Data Analyst
Organization: Emmvee Solar Systems Pvt. Ltd.

Purpose: Create comprehensive visualizations for solar energy analysis
================================================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Set clean visualization style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10

print("="*80)
print("COMPREHENSIVE SOLAR ENERGY ANALYSIS")
print("="*80)
print()

# ============================================================================
# LOAD DATA
# ============================================================================

print("Loading CSV file...")
df = pd.read_csv('weather_environmental_data.csv')
print(f"✓ Loaded {len(df)} hourly records")
print()

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# ============================================================================
# CHART 1: Cloud Cover vs Solar Irradiance
# ============================================================================

print("Creating Chart 1: Cloud Cover vs Solar Irradiance...")
fig, ax = plt.subplots(figsize=(14, 6))
ax.scatter(df['cloud_cover'], df['solar_irradiance'], 
           alpha=0.4, s=15, color='#34C759')
ax.set_xlabel('Cloud Cover (%)', fontsize=12, fontweight='500')
ax.set_ylabel('Solar Irradiance (W/m²)', fontsize=12, fontweight='500')
ax.set_title('Cloud Cover vs Solar Irradiance', fontsize=14, fontweight='600', pad=20)
ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('chart_1_cloud_irradiance.png', dpi=200, bbox_inches='tight')
plt.close()
print("✓ Saved: chart_1_cloud_irradiance.png")

# ============================================================================
# CHART 2: Monthly Average Solar Irradiance
# ============================================================================

print("Creating Chart 2: Monthly Average Solar Irradiance...")
monthly_avg = df.groupby('month')['solar_irradiance'].mean().reset_index()

fig, ax = plt.subplots(figsize=(14, 6))
ax.bar(monthly_avg['month'], monthly_avg['solar_irradiance'], 
       color='#FF9500', alpha=0.8, width=0.7)
ax.set_xlabel('Month', fontsize=12, fontweight='500')
ax.set_ylabel('Average Solar Irradiance (W/m²)', fontsize=12, fontweight='500')
ax.set_title('Monthly Average Solar Irradiance', fontsize=14, fontweight='600', pad=20)
ax.set_xticks(range(1, 13))
ax.set_xticklabels(month_names)
ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5, axis='y')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('chart_2_monthly_irradiance.png', dpi=200, bbox_inches='tight')
plt.close()
print("✓ Saved: chart_2_monthly_irradiance.png")

# ============================================================================
# CHART 3: Solar Irradiance Heatmap by Month and Hour
# ============================================================================

print("Creating Chart 3: Solar Irradiance Heatmap...")
pivot_data = df.groupby(['month', 'hour'])['solar_irradiance'].mean().reset_index()
heatmap_data = pivot_data.pivot(index='hour', columns='month', values='solar_irradiance')

# Convert hours to Indian time format
def hour_to_indian_time(hour):
    if hour == 0:
        return '12 AM'
    elif hour == 12:
        return '12 PM'
    elif hour > 12:
        return f'{hour-12} PM'
    else:
        return f'{hour} AM'

fig, ax = plt.subplots(figsize=(14, 8))
im = ax.imshow(heatmap_data, cmap='YlOrRd', aspect='auto', interpolation='nearest')
ax.set_xlabel('Month', fontsize=12, fontweight='500')
ax.set_ylabel('Time of Day (IST)', fontsize=12, fontweight='500')
ax.set_title('Solar Irradiance Heatmap: Hour vs Month', fontsize=14, fontweight='600', pad=20)
ax.set_xticks(range(12))
ax.set_xticklabels(month_names)
ax.set_yticks(range(0, 24))
ax.set_yticklabels([hour_to_indian_time(h) for h in range(0, 24)])
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Solar Irradiance (W/m²)', fontsize=11)
plt.tight_layout()
plt.savefig('chart_3_heatmap.png', dpi=200, bbox_inches='tight')
plt.close()
print("✓ Saved: chart_3_heatmap.png")

# ============================================================================
# CHART 4: Cloud Cover Impact on Solar Irradiance (Box Plot)
# ============================================================================

print("Creating Chart 4: Cloud Cover Impact Analysis...")
# Create cloud cover bins
df['cloud_bin'] = pd.cut(df['cloud_cover'], bins=[0, 20, 40, 60, 80, 100], 
                          labels=['0-20%', '20-40%', '40-60%', '60-80%', '80-100%'])

# Filter only daytime data (when solar irradiance > 0)
daytime_data = df[df['solar_irradiance'] > 0].copy()
cloud_groups = [daytime_data[daytime_data['cloud_bin'] == cat]['solar_irradiance'].values 
                for cat in ['0-20%', '20-40%', '40-60%', '60-80%', '80-100%']]

fig, ax = plt.subplots(figsize=(14, 6))
bp = ax.boxplot(cloud_groups, labels=['0-20%', '20-40%', '40-60%', '60-80%', '80-100%'],
                patch_artist=True, showfliers=False)
for patch in bp['boxes']:
    patch.set_facecolor('#34C759')
    patch.set_alpha(0.7)
for element in ['whiskers', 'fliers', 'means', 'medians', 'caps']:
    plt.setp(bp[element], color='#1d1d1f', linewidth=1.5)
ax.set_xlabel('Cloud Cover Range', fontsize=12, fontweight='500')
ax.set_ylabel('Solar Irradiance (W/m²)', fontsize=12, fontweight='500')
ax.set_title('Solar Irradiance Distribution by Cloud Cover Level', fontsize=14, fontweight='600', pad=20)
ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5, axis='y')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('chart_4_cloud_impact.png', dpi=200, bbox_inches='tight')
plt.close()
print("✓ Saved: chart_4_cloud_impact.png")

# ============================================================================
# CHART 5: Seasonal Solar Irradiance Comparison
# ============================================================================

print("Creating Chart 5: Seasonal Comparison...")
# Define seasons
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

df['season'] = df['month'].apply(get_season)
seasonal_avg = df.groupby('season')['solar_irradiance'].mean().reindex(['Winter', 'Spring', 'Summer', 'Fall'])

fig, ax = plt.subplots(figsize=(14, 6))
colors = ['#5AC8FA', '#34C759', '#FF9500', '#FF3B30']
bars = ax.bar(seasonal_avg.index, seasonal_avg.values, color=colors, alpha=0.8, width=0.6)
ax.set_xlabel('Season', fontsize=12, fontweight='500')
ax.set_ylabel('Average Solar Irradiance (W/m²)', fontsize=12, fontweight='500')
ax.set_title('Average Solar Irradiance by Season', fontsize=14, fontweight='600', pad=20)
ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5, axis='y')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.1f}',
            ha='center', va='bottom', fontsize=11, fontweight='600')
plt.tight_layout()
plt.savefig('chart_5_seasonal.png', dpi=200, bbox_inches='tight')
plt.close()
print("✓ Saved: chart_5_seasonal.png")

# ============================================================================
# CHART 6: Daily Solar Energy Potential (Peak Hours Analysis)
# ============================================================================

print("Creating Chart 6: Peak Hours Analysis...")
# Filter daytime hours (6 AM to 6 PM) with actual solar irradiance
daytime_df = df[(df['hour'] >= 6) & (df['hour'] <= 18) & (df['solar_irradiance'] > 0)]
hourly_avg = daytime_df.groupby('hour')['solar_irradiance'].mean().reset_index()

# Convert to Indian time format (12-hour with AM/PM)
def hour_to_indian_time(hour):
    if hour == 12:
        return '12 PM'
    elif hour > 12:
        return f'{hour-12} PM'
    else:
        return f'{hour} AM'

fig, ax = plt.subplots(figsize=(14, 6))
ax.fill_between(hourly_avg['hour'], hourly_avg['solar_irradiance'], 
                 alpha=0.25, color='#FF9500')
ax.plot(hourly_avg['hour'], hourly_avg['solar_irradiance'], 
        linewidth=3, color='#FF9500', marker='o', markersize=8)
ax.set_xlabel('Time of Day (IST)', fontsize=12, fontweight='500')
ax.set_ylabel('Average Solar Irradiance (W/m²)', fontsize=12, fontweight='500')
ax.set_title('Average Solar Irradiance by Hour (Daytime)', fontsize=14, fontweight='600', pad=20)
ax.set_xticks(hourly_avg['hour'])
ax.set_xticklabels([hour_to_indian_time(h) for h in hourly_avg['hour']], rotation=45, ha='right')
ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# Highlight peak hour
peak_hour = hourly_avg.loc[hourly_avg['solar_irradiance'].idxmax(), 'hour']
peak_time_label = hour_to_indian_time(int(peak_hour))
ax.axvline(x=peak_hour, color='#FF3B30', linestyle='--', linewidth=2, alpha=0.6, 
           label=f'Peak Hour: {peak_time_label}')
ax.legend(fontsize=11, loc='upper right')
plt.tight_layout()
plt.savefig('chart_6_peak_hours.png', dpi=200, bbox_inches='tight')
plt.close()
print("✓ Saved: chart_6_peak_hours.png")

# ============================================================================
# SUMMARY
# ============================================================================

print()
print("="*80)
print("ANALYSIS COMPLETE - 6 CHARTS GENERATED")
print("="*80)
print()
print("Charts Generated:")
print("  1. Cloud Cover vs Solar Irradiance (Scatter)")
print("  2. Monthly Average Solar Irradiance (Bar)")
print("  3. Solar Irradiance Heatmap: Hour vs Month")
print("  4. Cloud Cover Impact Analysis (Box Plot)")
print("  5. Seasonal Solar Irradiance Comparison")
print("  6. Peak Solar Hours Analysis")
print()
print("="*80)
