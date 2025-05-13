import json

# Sample dictionary
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "Data Analysis", "Machine Learning"],
    "is_employed": True
}

# Specify the file name
file_name = "data.json"

# Write the dictionary to a JSON file
with open(file_name, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"Dictionary has been written to {file_name}")

