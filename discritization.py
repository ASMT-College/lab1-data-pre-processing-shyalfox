import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv('./csv/sales_data.csv')
print("Initial Data:\n", df.head())

# Step 2: Apply discretization
bins = [0, 5000, 20000, float('inf')]
labels = ['Low', 'Medium', 'High']
df['SalesCategory'] = pd.cut(df['Sales'], bins=bins, labels=labels)

print("\nData after Discretization:\n", df.head())

# Step 3: Analyze the distribution of sales categories
sales_category_distribution = df['SalesCategory'].value_counts()
print("\nSales Category Distribution:\n", sales_category_distribution)