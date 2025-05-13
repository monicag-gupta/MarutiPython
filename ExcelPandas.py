Using Pandas and Excel(with atleast 10 data already entered: employees.xlsx file), provide a Menu Driven Program in Python for :
1. Adding a new Employee
2. Removing an Employee
3. Displaying the Employee List
4. Display the grouped departments and count of employees in each department
5. Display the statistics for the dataframe
6. Exit




import pandas as pd
import os

# File name
file_name = 'employees.xlsx'

# Load or create the DataFrame
if os.path.exists(file_name):
    df = pd.read_excel(file_name)
else:
    df = pd.DataFrame(columns=["ID", "Name", "Department", "Age", "Salary"])

def save_data(df):
    df.to_excel(file_name, index=False)

def add_employee(df):
    try:
        ID = int(input("Enter ID: "))
        if ID in df['ID'].values:
            print("Employee ID already exists.")
            return df
        Name = input("Enter Name: ")
        Department = input("Enter Department: ")
        Age = int(input("Enter Age: "))
        Salary = float(input("Enter Salary: "))
        new_row = pd.DataFrame([[ID, Name, Department, Age, Salary]], columns=df.columns)
        df = pd.concat([df, new_row], ignore_index=True)
        save_data(df)
        print("Employee added successfully.\n")
    except Exception as e:
        print("Error:", e)
    return df

def remove_employee(df):
    try:
        ID = int(input("Enter Employee ID to remove: "))
        if ID not in df['ID'].values:
            print("Employee ID not found.")
            return df
        df = df[df['ID'] != ID]
        save_data(df)
        print("Employee removed successfully.\n")
    except Exception as e:
        print("Error:", e)
    return df

def display_employees(df):
    print("\nEmployee List:")
    print(df.to_string(index=False))

def group_by_department(df):
    print("\nEmployees by Department:")
    grouped = df.groupby('Department')['Name'].count()
    print(grouped)

def display_statistics(df):
    print("\nStatistics:")
    print(df.describe(include='all'))

def menu(df):
    while True:
        print("\n--- Employee Management Menu ---")
        print("1. Add a new Employee")
        print("2. Remove an Employee")
        print("3. Display Employee List")
        print("4. Grouped Departments and Count")
        print("5. Display Statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            df = add_employee(df)
        elif choice == '2':
            df = remove_employee(df)
        elif choice == '3':
            display_employees(df)
        elif choice == '4':
            group_by_department(df)
        elif choice == '5':
            display_statistics(df)
        elif choice == '6':
            print("Exiting Program.")
            break
        else:
            print("Invalid choice. Try again.")

# Run the menu
menu(df)

