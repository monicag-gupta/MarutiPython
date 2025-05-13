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

