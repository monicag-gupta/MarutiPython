# Example set
my_set = {10, 20, 30, 40, 50}
another_set = {30, 40, 50, 60, 70}
yet_another_set = {100, 200}

# Displaying the set (properties)
print("Original set:", my_set)

# 1. Basic Operations
my_set.add(60)  # Add an element
print("After adding 60:", my_set)

my_set.remove(20)  # Remove an element
print("After removing 20:", my_set)

my_set.discard(100)  # Discard an element (does not raise an error if not found)
print("After discarding 100:", my_set)

popped_element = my_set.pop()  # Remove and return a random element
print("Popped element:", popped_element)
print("After popping an element:", my_set)

my_set.clear()  # Clear the set
print("After clearing the set:", my_set)

# Reinitialize the set for further examples
my_set = {10, 20, 30, 40, 50}

# 2. Mathematical Operations
union_set = my_set.union(another_set)  # Union
print("Union of sets:", union_set)

intersection_set = my_set.intersection(another_set)  # Intersection
print("Intersection of sets:", intersection_set)

difference_set = my_set.difference(another_set)  # Difference
print("Difference of sets:", difference_set)

symmetric_difference_set = my_set.symmetric_difference(another_set)  # Symmetric Difference
print("Symmetric difference of sets:", symmetric_difference_set)

# 3. Methods for Comparison
is_disjoint = my_set.isdisjoint(yet_another_set)  # Check if disjoint
print("Is disjoint with yet_another_set?", is_disjoint)

is_subset = my_set.issubset(union_set)  # Check if subset
print("Is my_set a subset of union_set?", is_subset)

is_superset = union_set.issuperset(my_set)  # Check if superset
print("Is union_set a superset of my_set?", is_superset)

# 4. Other Methods
copied_set = my_set.copy()  # Copy the set
print("Copied set:", copied_set)

my_set.update(another_set)  # Update the set with another set
print("After updating my_set with another_set:", my_set)

my_set.intersection_update(another_set)  # Update with intersection
print("After intersection_update with another_set:", my_set)

my_set.difference_update(another_set)  # Update with difference
print("After difference_update with another_set:", my_set)

my_set.symmetric_difference_update(another_set)  # Update with symmetric difference
print("After symmetric_difference_update with another_set:", my_set)

# 5. Length and Membership Testing
my_set = {10, 20, 30, 40, 50}
print("Length of my_set:", len(my_set))  # Length of the set
print("Is 20 in my_set?", 20 in my_set)  # Membership testing
print("Is 100 not in my_set?", 100 not in my_set)  # Membership testing

# 6. Mathematical Operators
print("Union using |:", my_set | another_set)
print("Intersection using &:", my_set & another_set)
print("Difference using -:", my_set - another_set)
print("Symmetric difference using ^:", my_set ^ another_set)

