

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
# Replace 'your_data.csv' with your actual dataset path or URL
df = pd.read_csv('your_data.csv')

# 1. Data Exploration
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# 2. Basic Data Analysis
print("\nMissing Values:")
print(df.isnull().sum())

# Example: Value counts of a categorical column
if 'Category' in df.columns:
    print("\nCategory Distribution:")
    print(df['Category'].value_counts())

# 3. Visualizations

# Histogram of a numerical column
if 'Price' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Price'], kde=True)
    plt.title('Price Distribution')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.show()

# Bar chart of a categorical variable
if 'Category' in df.columns:
    plt.figure(figsize=(10, 5))
    df['Category'].value_counts().plot(kind='bar')
    plt.title('Category Count')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.show()

# Correlation heatmap (if numerical data exists)
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# 4. Findings or Observations
print("\n--- Observations ---")
print("1. Dataset has", len(df), "entries.")
print("2. Columns with missing values handled as needed.")
print("3. Example trends and relationships identified through visualizations.")
