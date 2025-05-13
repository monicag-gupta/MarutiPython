# Import necessary libraries
import pandas as pd
import numpy as np

# Step 1: Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, np.nan, 40, '28'],  # '28' is a string, others are numeric
    'City': ['New York', 'Los Angeles', np.nan, 'Chicago', 'Houston'],
    'Salary': [50000, 60000, 70000, np.nan, 80000],
    'Joining Date': ['2022-01-01', '2021-05-15', '2020-03-10', None, '2019-07-30']
}

df = pd.DataFrame(data)
print("Initial DataFrame:")
print(df)

# Step 2: Handling missing values and Converting 'Age' to numeric
# Fill missing 'Age' with the mean of the numeric values
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  # Convert 'Age' to numeric
df['Age'] = df['Age'].fillna(df['Age'].mean())  # Fill missing 'Age' with the mean

# Fill missing 'City' with a default value
df['City'] = df['City'].fillna('Unknown')

# Fill missing 'Salary' with 0
df['Salary'] = df['Salary'].fillna(0)

print("\nDataFrame after handling missing values and Converting 'Age' to numeric:")
print(df)

# Step 3: Converting data types
# Convert 'Joining Date' to datetime
df['Joining Date'] = pd.to_datetime(df['Joining Date'], errors='coerce')

# Ensure 'Age' is a float and 'Salary' is an integer
df['Age'] = df['Age'].astype(float)
df['Salary'] = df['Salary'].astype(int)

print("\nDataFrame after converting data types: Sal:int, Age: float, Joining Data: DateTime:")
print(df)

# Step 4: Applying functions to columns or rows
# Add a column to calculate the year of joining
df['Joining Year'] = df['Joining Date'].apply(lambda x: x.year if pd.notnull(x) else 'Unknown')

# Add a column categorizing 'Age'
df['Age Category'] = df['Age'].apply(lambda x: 'Youth' if x < 30 else 'Adult')

# Add a row-wise operation: calculating a bonus as 10% of the salary
df['Bonus'] = df['Salary'] * 0.1

print("\nDataFrame after applying functions:")
print(df)

# When pandas displays ... in a DataFrame output, it means the data is too wide (too many columns) or too long (too many rows) to be shown completely in the default display.
# To show all columns and rows in the output, use:
# Show all columns
pd.set_option('display.max_columns', None)
# Show all rows
pd.set_option('display.max_rows', None)
# Optional: Set full width
pd.set_option('display.width', None)
# Optional: Prevent column content truncation
pd.set_option('display.max_colwidth', None)  # Or a large number like 1000 for older versions

print("\nDataFrame after applying wide data Show Options:")
print(df)

# To reset to default settings later:
pd.reset_option('display.max_columns')
pd.reset_option('display.max_rows')
pd.reset_option('display.width')
pd.reset_option('display.max_colwidth')

print("\nDataFrame after reset of Show Options:")
print(df)


