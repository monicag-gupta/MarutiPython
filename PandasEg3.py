import pandas as pd

# Step 1: Create a simple DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 22],
    "Salary": [50000, 60000, 70000, 80000, 40000],
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
# Step 2: Conditional update - Increase salary by 10% for people aged 30 or above
# .loc[] is used to access specific rows and columns by label.
df.loc[df["Age"] >= 30, "Salary"] = df["Salary"] * 1.10
print("\nDataFrame after conditional salary update:\n", df)
# Step 3: Add a new column with calculated data - Bonus (10% of salary)
df["Bonus"] = df["Salary"] * 0.10
print("\nDataFrame after adding calculated Bonus column:\n", df)
# Step 4: Conditional update - Give a bonus of 5000 for people earning less than 50,000
df.loc[df["Salary"] < 50000, "Bonus"] = 5000
print("\nDataFrame after conditional bonus update:\n", df)










##################3



import pandas as pd

# Step 1: Create two DataFrames
data1 = {
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Alice", "Bob", "Charlie", "David", "John", "Jane", "Sue", "Nany"],
    "Department": ["HR", "Finance", "IT", "HR", "HR", "IT", "HR", "IT"],
}

data2 = {
    "Employee_ID": [101, 102, 105, 106, 108, 110],
    "Salary": [60000, 70000, 80000, 75000, 89000, 45000],
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("DataFrame 1 (Employee Info):")
print(df1)
print("\nDataFrame 2 (Salary Info):")
print(df2)

# Step 2: GroupBy - Count employees by department
department_counts = df1.groupby("Department")["Employee_ID"].count()
print("\nEmployee count by department:")
print(department_counts)

# Step 3: Merging - Merge the two DataFrames based on Employee_ID
merged_df = pd.merge(df1, df2, on="Employee_ID", how="inner")
print("\nInner Merged DataFrame (Employee info with salary):")
print(merged_df)

merged_df = pd.merge(df1, df2, on="Employee_ID", how="left")
print("\nLeft Merged DataFrame (Employee info with salary):")
print(merged_df)

merged_df = pd.merge(df1, df2, on="Employee_ID", how="right")
print("\nRight Merged DataFrame (Employee info with salary):")
print(merged_df)

merged_df = pd.merge(df1, df2, on="Employee_ID", how="outer")
print("\nOuter Merged DataFrame (Employee info with salary):")
print(merged_df)

# Step 4: Joining - Join two DataFrames based on index
# For this to work, we set an index
df1.set_index("Employee_ID", inplace=True)
df2.set_index("Employee_ID", inplace=True)

print("\nDataFrame 1 Index set as Employee_ID:");print(df1)
print("\nDataFrame 2 Index set as Employee_ID:");print(df2)

joined_df = df1.join(df2, how="left")
print("\nLeft Joined DataFrame (Employee info with salary):")
print(joined_df)

joined_df = df1.join(df2, how="right")
print("\nRight Joined DataFrame (Employee info with salary):")
print(joined_df)

joined_df = df1.join(df2, how="inner")
print("\nInner Joined DataFrame (Employee info with salary):")
print(joined_df)

joined_df = df1.join(df2, how="outer")
print("\nOuter Joined DataFrame (Employee info with salary):")
print(joined_df)






###########


import pandas as pd

# Sample DataFrame
data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'John'],
    'Department': ['HR', 'Finance', 'IT', 'HR', 'HR', 'IT', 'Finance'],
    'Salary': [60000, 70000, 80000, 65000, 75000, 85000, 89000],
    'Age': [25, 30, 35, 40, 25, 35, 50]
}

df = pd.DataFrame(data)

# Group by 'Department' and apply aggregation functions

print("\nEmployee count by department:")
print(df.groupby("Department")["Employee_ID"].count())

print("Group by Department - Salary Sum:")
print(df.groupby('Department')['Salary'].sum())

print("\nGroup by Department - Salary Mean:")
print(df.groupby('Department')['Salary'].mean())

print("\nGroup by Department - Salary Median:")
print(df.groupby('Department')['Salary'].median())

print("\nGroup by Department - Salary Min:")
print(df.groupby('Department')['Salary'].min())

print("\nGroup by Department - Salary Max:")
print(df.groupby('Department')['Salary'].max())

print("\nGroup by Department - Salary Standard Deviation:")
print(df.groupby('Department')['Salary'].std())

print("\nGroup by Department - Salary Standard Variance:")
print(df.groupby('Department')['Salary'].var())

print("\nGroup by Department - First salary in group:")
print(df.groupby('Department')['Salary'].first())

print("\nGroup by Department - Last salary in group:")
print(df.groupby('Department')['Salary'].last())

print("\nGroup by Department - Custom Aggregation (Min and Max):")
print(df.groupby('Department').agg({
    'Salary': ['min', 'max'],
    'Age': 'mean'
}))

print("\nGroup by Department - Custom Function(max-min) to group:")
print(df.groupby('Department')['Salary'].apply(lambda x: x.max() - x.min()))

print("\nGroup by Department - transform to a new dataframe with same size as df:")
print(df.groupby('Department')['Salary'].transform(lambda x: x - x.mean()))

print("\nGroup by Department - size of each row:")
print(df.groupby('Department')['Salary'].size())

print("\nGroup by Department - Cross-tabulation of two or more variables:")
print(pd.crosstab(df['Department'], df['Age']))

print("\nGroup by Department - statistics for each group (count, mean, std, min, 25%, 50%, 75%, and max:")
print(df.groupby('Department').describe())

print("\nGroup by Department - Filter Groups with Mean Salary > 70000:")
print(df.groupby('Department').filter(lambda x: x['Salary'].mean() > 70000))


