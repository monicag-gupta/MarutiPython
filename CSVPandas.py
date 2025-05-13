employees.csv

Name,Age,Department,Salary,Joining Date
Alice,25,HR,50000,2022-01-01
Bob,30,IT,60000,2021-05-15
Charlie,35,Finance,70000,2020-03-10
David,40,IT,80000,2019-07-30
Eve,28,HR,55000,2023-02-15





# Import necessary libraries
import pandas as pd

# Step 1: Read the CSV file
# Assume the file 'employees.csv' contains sample employee data
# CSV Example Content:
# Name,Age,Department,Salary,Joining Date
# Alice,25,HR,50000,2022-01-01
# Bob,30,IT,60000,2021-05-15
# Charlie,35,Finance,70000,2020-03-10
# David,40,IT,80000,2019-07-30
# Eve,28,HR,55000,2023-02-15

# Read the CSV file into a DataFrame
df = pd.read_csv('employees.csv')

# Step 2: Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Step 3: Get a summary of the data
print("\nSummary of the data:")
print(df.info())

# Step 4: Display basic statistics of numeric columns
print("\nBasic statistics of numeric columns:")
print(df.describe())

# Step 5: Perform basic manipulations
# Filter employees in the 'IT' department
it_employees = df[df['Department'] == 'IT']
print("\nEmployees in the IT Department:")
print(it_employees)

# Calculate the average salary of employees
average_salary = df['Salary'].mean()
print(f"\nAverage salary of employees: {average_salary}")

# Add a new column for years since joining
df['Years Since Joining'] = pd.to_datetime('today').year - pd.to_datetime(df['Joining Date']).dt.year
print("\nDataFrame with 'Years Since Joining':")
print(df)

# Step 6: Save the modified DataFrame to a new CSV file
df.to_csv('modified_employees.csv', index=False)
print("\nModified DataFrame saved to 'modified_employees.csv'")








