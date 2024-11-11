import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv('./csv/customer_ages.csv')
print("Initial Data:\n", df.head())

# Step 2: Create bins and assign labels
bins = [18, 30, 50, 100]
labels = ['Young', 'Middle-aged', 'Senior']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

print("\nData after Binning:\n", df.head())

# Step 3: Calculate distribution of customers in each age group
age_group_distribution = df['AgeGroup'].value_counts()
print("\nAge Group Distribution:\n", age_group_distribution)