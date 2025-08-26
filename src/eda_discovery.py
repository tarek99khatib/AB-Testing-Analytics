import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ab_testing_analytics/data/processed/daily_stats.csv")

print(df.head(5))
print(df.info())
df['date'] = pd.to_datetime(df['date'])
df.sort_values(by='date', inplace=True)

# data for treatment groups
df_treatment = df[df['group_name'] == 'treatment']

# data for control group
df_control = df[df['group_name'] == 'control']



# Plot both groups on the same chart
plt.close() # close any previous plots
plt.figure(figsize=(12, 6))

plt.plot(df_treatment['date'], df_treatment['conversion_rate'], 
         marker='o', linestyle='-', color='blue', label='Treatment')

plt.plot(df_control['date'], df_control['conversion_rate'], 
         marker='o', linestyle='-', color='red', label='Control')

plt.title('Daily Conversion Rates: Treatment vs Control')
plt.xlabel('Date')
plt.ylabel('Conversion Rate (%)')
plt.xticks(rotation=45)
plt.legend()  
plt.tight_layout()
plt.savefig("ab_testing_analytics/figures/daily_conversion_rates_compare.png")
plt.close()
# insight 1: they are very similar


# plot overall conversion rates for both groups
plt.close() # close any previous plots
plt.figure(figsize=(8, 6))
plt.bar(['Treatment', 'Control'], 
        [df_treatment['conversion_rate'].mean(), df_control['conversion_rate'].mean()], 
        color=['blue', 'red'])
plt.title('Overall Conversion Rates: Treatment vs Control')
plt.ylabel('Average Conversion Rate (%)')
plt.tight_layout()
plt.savefig("ab_testing_analytics/figures/overall_conversion_rates_compare.png")
plt.close() 
# insight 2: they are very similar

# Histogram of conversion rates by group
plt.close()
plt.figure(figsize=(10,6))

plt.hist(df_treatment['conversion_rate'], bins=20, alpha=0.7, color='blue', label='Treatment')
plt.hist(df_control['conversion_rate'], bins=20, alpha=0.7, color='red', label='Control')

plt.title('Histogram of Daily Conversion Rates')
plt.xlabel('Conversion Rate (%)')
plt.ylabel('Frequency')
plt.legend() 
plt.tight_layout()
plt.savefig("ab_testing_analytics/figures/histogram_conversion_rates.png")
plt.close()
# insight 3: there is a chance the control group has a higher conversion rate



# --- Boxplot for conversion rates ---

plt.close()
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x="group_name", y="conversion_rate", palette=["red", "blue"])
plt.title("Boxplot of Conversion Rates by Group")
plt.xlabel("Group")
plt.ylabel("Conversion Rate (%)")
plt.tight_layout()
plt.savefig("ab_testing_analytics/figures/conversion_rate_boxplot.png")
plt.close()

# --- Summary statistics ---
summary_stats = df.groupby("group_name")["conversion_rate"].describe()
print("\n📊 Summary Statistics by Group:")
print(summary_stats)
summary_stats.to_csv("ab_testing_analytics/data/processed/conversion_rate_summary.csv")