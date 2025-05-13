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



#####################

import json

# Specify the file name
file_name = "data.json"

# Read the JSON file
with open(file_name, 'r') as json_file:
    data = json.load(json_file)

# Print the dictionary
print("Data read from JSON file:")
print(data)

# Pretty print the JSON data
print("\nData as JSON printed in pretty format:")
print(json.dumps(data, indent=4))







