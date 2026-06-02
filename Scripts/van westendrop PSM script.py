#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 22:18:02 2026

@author: as
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 00:08:14 2026

@author: as
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

print("Starting the refined Van Westendorp analysis...")

# --- 1. SETUP RELATIVE PATHS (Fixes local path dependency) ---
# Gets the absolute directory path where this script file is currently located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Map paths to look inside a 'Data' folder relative to the script location
file_eng = os.path.join(script_dir, "Data", "Eng From free to fee responses.xlsx")
file_rom = os.path.join(script_dir, "Data", "ro_data.xlsx")

# Ensure an 'Outputs' directory exists next to the script to save the final graph
output_dir = os.path.join(script_dir, 'Outputs')
os.makedirs(output_dir, exist_ok=True)

# --- 2. EXTRACT ONLY THE NUMERICAL PSM DATA ---
print("Loading and extracting pricing columns...")
# Extracting the last 4 columns from both files
df_eng = pd.read_excel(file_eng).iloc[:, -4:]
df_ro = pd.read_excel(file_rom).iloc[:, -4:]

# Rename columns uniformly
standard_cols = ['Too_Cheap', 'Bargain', 'Expensive', 'Too_Expensive']
df_eng.columns = standard_cols
df_ro.columns = standard_cols

# Combine datasets
df_all = pd.concat([df_eng, df_ro], ignore_index=True)

# --- 3. THE LOGIC SCRUB ---
# Convert text/blanks to NaN, then drop missing rows
for col in standard_cols:
    df_all[col] = pd.to_numeric(df_all[col], errors='coerce')

df_clean = df_all.dropna().copy()

# Enforce standard pricing logic
valid_logic = (
    (df_clean['Too_Cheap'] <= df_clean['Bargain']) &
    (df_clean['Bargain'] <= df_clean['Expensive']) &
    (df_clean['Expensive'] <= df_clean['Too_Expensive'])
)
df_logic = df_clean[valid_logic].copy()

# --- 4. STATISTICAL OUTLIER FILTERING ---
print("Filtering out absurd values and extreme outliers...")

# Calculate the Interquartile Range (IQR) for the highest boundary ('Too_Expensive')
Q1 = df_logic['Too_Expensive'].quantile(0.25)
Q3 = df_logic['Too_Expensive'].quantile(0.75)
IQR = Q3 - Q1

# Set a generous upper limit (Q3 + 2.0 * IQR)
upper_bound = Q3 + (2.0 * IQR)

# Filter out any absurd base prices (e.g., someone putting less than $1 as 'Bargain')
not_troll_high = df_logic['Too_Expensive'] <= upper_bound
not_troll_low = df_logic['Bargain'] > 1 

df_final = df_logic[not_troll_high & not_troll_low].copy()

# Print the cleaning stats to the console
print("-" * 30)
print(f"Initial raw rows: {len(df_all)}")
print(f"Rows after Logic Scrub: {len(df_logic)}")
print(f"Final valid rows after Outlier Filter: {len(df_final)}")
print(f"Removed {len(df_logic) - len(df_final)} extreme outliers.")
print("-" * 30)

# --- 5. CALCULATE CUMULATIVE FREQUENCIES ---
prices = np.unique(df_final.values)
prices = np.sort(prices)

tc_curve, b_curve, e_curve, te_curve = [], [], [], []
n = len(df_final)

for p in prices:
    tc_curve.append(sum(df_final['Too_Cheap'] >= p) / n)
    b_curve.append(sum(df_final['Bargain'] >= p) / n)
    e_curve.append(sum(df_final['Expensive'] <= p) / n)
    te_curve.append(sum(df_final['Too_Expensive'] <= p) / n)

# --- 6. PLOT THE PSM GRAPH ---
print("Generating the Van Westendorp graph...")
plt.figure(figsize=(10, 6), dpi=150)

plt.plot(prices, tc_curve, label='Too Cheap', color='blue', linestyle='--')
plt.plot(prices, b_curve, label='Cheap (Bargain)', color='green')
plt.plot(prices, e_curve, label='Expensive', color='orange')
plt.plot(prices, te_curve, label='Too Expensive', color='red', linestyle='--')

# X-axis dynamically scales to the max valid price
plt.xlim(0, max(prices))

plt.title('Van Westendorp Price Sensitivity Meter', fontsize=14, fontweight='bold')
plt.xlabel('Monthly Subscription Price (USD)', fontsize=12)
plt.ylabel('Proportion of Respondents', fontsize=12)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4)
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Save the image automatically to the Outputs folder
output_image = os.path.join(output_dir, "PSM_Graph_Refined.png")
plt.savefig(output_image)

plt.show()
print(f"Done! The refined chart is saved cleanly to: {output_image}")