import pandas as pd
# Step 1: Load the dataset
df = pd.read_csv('./csv/employee_data.csv')
print("Initial Data:\n", df.head())
# Step 2: Handle missing values# Fill missing 'Age' with the mean age and 'Salary' with the mean salary
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
# Step 3: Standardize department names
df['Department'] = df['Department'].replace({
    'Human Resources': 'HR',
    'H.R.': 'HR',
    'hr': 'HR'
})
# Step 4: Remove duplicate records based on 'ID'
df.drop_duplicates(subset='ID', keep='first', inplace=True)
print("\nCleaned Data:\n", df.head())