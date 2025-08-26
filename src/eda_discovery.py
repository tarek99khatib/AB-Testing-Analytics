import pandas as pd
import matplotlib.pyplot as plt
plt.close()  # close any previous plots

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
