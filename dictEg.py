# Example Dictionary
my_dict = { "name": "Alice", "age": 25, "skills": ["Python", "Data Analysis"], "is_student": False}

# Display the dictionary (properties)
print("Original Dictionary:", my_dict)

# 1. Accessing Values
print("Access 'name':", my_dict["name"])
print("Access with get('age'):", my_dict.get("age"))

# 2. Adding Key-Value Pairs
my_dict["city"] = "New York"
print("After adding city:", my_dict)

# 3. Updating Values
my_dict["age"] = 26
print("After updating age:", my_dict)

# 4. Deleting Key-Value Pairs
del my_dict["is_student"]
print("After deleting is_student:", my_dict)

# 5. Using pop() to remove an item
popped_item = my_dict.pop("city")
print("Popped item (city):", popped_item)
print("After popping city:", my_dict)

# 6. Using popitem() to remove the last inserted item
popped_item = my_dict.popitem()
print("Popped last item:", popped_item)
print("After popping last item:", my_dict)

# 7. Using setdefault() to get a value or set default
default_value = my_dict.setdefault("country", "USA")
print("Set default for 'country':", default_value)
print("After setdefault:", my_dict)

# 8. Merging Dictionaries
additional_data = {"hobby": "Reading", "profession": "Engineer"}
my_dict.update(additional_data)
print("After updating with additional_data:", my_dict)

# 9. Accessing Keys, Values, and Items
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

# 10. Iterating through the Dictionary
print("Iterating through keys and values:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 11. Checking Key Existence
print("Is 'name' in my_dict?", "name" in my_dict)
print("Is 'salary' not in my_dict?", "salary" not in my_dict)

# 12. Copying the Dictionary
copied_dict = my_dict.copy()
print("Copied Dictionary:", copied_dict)

# 13. Clearing the Dictionary
my_dict.clear()
print("After clearing:", my_dict)
