import pandas as pd

# Load dataset 
df = pd.read_csv('globalterrorismdb_0522dist.csv')

# Display basic information about the dataset
print(df.info())
print(df.head())
print(df.isnull().sum())
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)

#Drop irralevant columns 
df.drop(['alternative', 'alternative_txt'], axis=1, inplace=True)

#Fill missing values
df['latitude'].fillna(df['latitude'].mean(), inplace=True)
df['longitude'].fillna(df['longitude'].mean(), inplace=True)

#Rename columns for clarity
df.rename(columns={'country_txt': 'country'}, inplace=True)
import os

# Define the directory path
data_dir = 'data'

# Check if the directory exists, if not, create it
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

#Save the cleaned data
cleaned_file_path = os.path.join(data_dir, 'cleaned_global_terrorism.csv')
df.to_csv(cleaned_file_path, index=False)
print(f"File saved successfully at {cleaned_file_path}")

import pandas as pd
import os

import pandas as pd

# Load the dataset (replace 'path_to_file' with the actual file path of your dataset)
# Use 'latin1' encoding because this dataset often contains special characters
df = pd.read_csv('data/cleaned_global_terrorism.csv', encoding='latin1')

# Display basic information about the dataset
print("Dataset Information:")
print(df.info())

# Display the first few rows of the dataset
print("\nFirst 5 Rows of the Dataset:")
print(df.head())


# Define the directory and file name
data_dir = 'data'
cleaned_file_name = 'cleaned_global_terrorism.csv'

# Ensure the directory exists
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Save the cleaned data
cleaned_file_path = os.path.join(data_dir, cleaned_file_name)
df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved successfully at {cleaned_file_path}")





