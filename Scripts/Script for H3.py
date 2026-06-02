#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 22:15:55 2026

@author: as
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 19:30:38 2026

@author: as
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# 1. Setup Relative Paths (Fixes local path dependency)
# Gets the absolute directory path where this script file is currently located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Look for 'H3_Data.xlsx' inside a folder named 'Data' relative to the script
file_path = os.path.join(script_dir, 'Data', 'H3_Data.xlsx') 
df = pd.read_excel(file_path)

# Ensure an 'Outputs' directory exists next to the script to save the final graph
output_dir = os.path.join(script_dir, 'Outputs')
os.makedirs(output_dir, exist_ok=True)

# 2. Grouping Logic for H3
# We define which fields are "High-Stakes"
high_stakes = ['Legal/Compliance', 'Healthcare', 'Business/Finance']

def categorize_stake(field):
    if field in high_stakes:
        return 'High-Stakes (Legal/Med/Fin)'
    else:
        return 'General (Tech/Creative/Academia)'

df['Stake_Level'] = df['Professional_Field'].apply(categorize_stake)

# 3. Create the Contingency Table
# We compare Stake_Level vs. the Choice from Item 15
ctab = pd.crosstab(df['Stake_Level'], df['Privacy_Choice'])

# 4. Statistical Test (Chi-Square)
chi2, p, dof, expected = chi2_contingency(ctab)

print("--- Contingency Table (Counts) ---")
print(ctab)
print(f"\nChi-Square p-value: {p:.4f}")

# 5. Visualization for Dissertation
# We turn counts into percentages for a better chart
ctab_pct = ctab.div(ctab.sum(axis=1), axis=0) * 100

ax = ctab_pct.plot(kind='bar', stacked=False, figsize=(10,6), color=['#e74c3c', '#2ecc71', '#95a5a6'])
plt.title('H3: Privacy Choice by Professional Stake Level', fontsize=14)
plt.ylabel('Percentage of Group (%)')
plt.xlabel('Professional Category')
plt.xticks(rotation=0)
plt.legend(title='Choice (Item 15)')

# Add percentage labels on bars
for p_bar in ax.patches:
    width = p_bar.get_width()
    height = p_bar.get_height()
    x, y = p_bar.get_xy() 
    if height > 0:
        ax.annotate(f'{height:.1f}%', (x + width/2, y + height*1.02), ha='center')

plt.tight_layout()

# Save the plot directly into the newly created Outputs folder
chart_output_path = os.path.join(output_dir, 'H3_Results_Chart.png')
plt.savefig(chart_output_path, dpi=300)
print(f"\nAnalysis complete. Plot saved cleanly to: {chart_output_path}")

plt.show()