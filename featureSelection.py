from sklearn.feature_selection import SelectKBest, chi2
import numpy as np
import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv('./csv/medical_data.csv')
print("Initial Data:\n", df.head())

# Step 2: Define features and target variable
X = df.drop(columns=['Disease'])
y = df['Disease']

# Step 3: Apply Chi-square feature selection
selector = SelectKBest(score_func=chi2, k=3)
selector.fit(X, y)

# Step 4: Get the top 3 features
top_features = X.columns[selector.get_support()]
print("\nTop 3 Features for Predicting Disease:\n", top_features)