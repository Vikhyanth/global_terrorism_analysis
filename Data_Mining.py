import pandas as pd
from sklearn.cluster import KMeans
import os

# Step 1: Verify file existence and load dataset
file_path = 'data/cleaned_global_terrorism.csv'
if os.path.exists(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully.")
        print(df.head())
    except Exception as e:
        print(f"Error loading dataset: {e}")
else:
    print(f"File not found at: {file_path}. Please check.")
    exit()  # Exit script if file is missing

# Step 2: Perform clustering if required columns exist
if 'latitude' in df.columns and 'longitude' in df.columns:
    try:
        features = df[['latitude', 'longitude']].dropna()
        kmeans = KMeans(n_clusters=5, random_state=42)
        df['cluster'] = kmeans.fit_predict(features)
        df.to_csv('data/clustered_data.csv', index=False)
        print("Clustering complete. Results saved to 'data/clustered_data.csv'.")
    except Exception as e:
        print(f"Error during clustering: {e}")
else:
    print("Error: Required columns ('latitude', 'longitude') are missing from the dataset.")

# predictive modelling
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X = df[['attacktype1', 'suicide']]
y = df['success']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)
print("Model Accuracy:", model.score(X_test, y_test))
