import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm 


df = pd.read_csv("ab_testing_analytics/data/processed/daily_stats.csv")

df['date'] = pd.to_datetime(df['date'])
df.sort_values(by='date', inplace=True)

# data for treatment groups
df_treatment = df[df['group_name'] == 'treatment']

# data for control group
df_control = df[df['group_name'] == 'control']

total_users_treatment = df_treatment['total_users_in_group'].sum()
total_users_control = df_control['total_users_in_group'].sum()
total_conversions_treatment = df_treatment['converted_users_in_group'].sum()
total_conversions_control = df_control['converted_users_in_group'].sum()

p1, p2 = total_conversions_control / total_users_control, total_conversions_treatment / total_users_treatment

# Pooled probability
p_pool = (total_conversions_control + total_conversions_treatment) / (total_users_control + total_users_treatment)

# Standard error
SE = np.sqrt(p_pool * (1 - p_pool) * (1/total_users_control + 1/total_users_treatment))

# Z-score
Z = (p1 - p2) / SE

# P-value (two-tailed)
p_value = 2 * (1 - norm.cdf(abs(Z)))

print("\nControl CR = {p1:.4f} | Treatment CR = {p2:.4f}")
print("Z = {Z:.3f}")
print("P-value = {p_value:.4f}")

if p_value < 0.05:
    print("✅ Significant difference between groups!")
else:
    print("❌ No significant difference, likely random.")