#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 22:16:55 2026

@author: as
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Setup Relative Paths (Fixes local path dependency)
# Gets the absolute directory path where this script file is currently located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Look for 'Q18.xlsx' inside a folder named 'Data' relative to the script
file_name = 'Q18.xlsx' 
file_path = os.path.join(script_dir, 'Data', file_name) 

# Load the file
df = pd.read_excel(file_path)

# Ensure an 'Outputs' directory exists next to the script to save the final graph
output_dir = os.path.join(script_dir, 'Outputs')
os.makedirs(output_dir, exist_ok=True)

# Identify the column (adjust if the name is different in your file)
col_name = df.columns[0]

# 2. Process Multi-Response Data
df_clean = df[col_name].fillna('None')
all_selections = df_clean.str.split(', ')
exploded = all_selections.explode().str.strip()

# 3. Calculate Counts and Percentages
total_n = len(df)
counts = exploded.value_counts()
percentages = (counts / total_n) * 100

# 4. Display Results in the Console
print("--- Refusal Frequencies ---")
print(counts)
print("\n--- Percentages (N={}) ---".format(total_n))
print(percentages.round(2))

# 5. Create and Show the Plot
plt.figure(figsize=(10, 6))
percentages.sort_values().plot(kind='barh', color='skyblue', edgecolor='black')
plt.title('H2: Refusal to Use Free AI for Specific Tasks (N=302)')
plt.xlabel('Percentage of Respondents (%)')
plt.ylabel('Task Category')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the plot directly into the newly created Outputs folder
plot_path = os.path.join(output_dir, 'Hypothesis_2_Plot.png')
plt.savefig(plot_path, dpi=300)
print(f"\nAnalysis complete. Plot saved cleanly to: {plot_path}")

plt.show()