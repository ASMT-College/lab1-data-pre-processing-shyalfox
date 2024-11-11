import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Step 1: Load the dataset
df = pd.read_csv('./csv/student_scores.csv')
print("Initial Data:\n", df.head())

# Step 2: Apply Min-Max normalization
scaler = MinMaxScaler()
df[['Math', 'Science', 'English']] = scaler.fit_transform(df[['Math', 'Science', 'English']])

print("\nNormalized Scores:\n", df.head())