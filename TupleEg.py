# Tuple declaration
my_tuple = (10, 20, 30, 40, 50)
print("Original Tuple:", my_tuple)

# Properties of tuples
print("\nProperties:")
print("Length of tuple:", len(my_tuple))  # Length of the tuple
print("Minimum value in the tuple:", min(my_tuple))  # Minimum value
print("Maximum value in the tuple:", max(my_tuple))  # Maximum value
print("Sum of all elements in the tuple:", sum(my_tuple))  # Sum of elements

# Accessing elements
print("\nAccessing Elements:")
print("First element:", my_tuple[0])  # Access the first element
print("Last element:", my_tuple[-1])  # Access the last element
print("Slice from index 1 to 3:", my_tuple[1:4])  # Slice elements
print("Every second element:", my_tuple[::2])  # Step through elements

# Tuple concatenation and repetition
print("\nConcatenation and Repetition:")
another_tuple = (60, 70)
concatenated_tuple = my_tuple + another_tuple  # Concatenate two tuples
print("Concatenated tuple:", concatenated_tuple)

repeated_tuple = my_tuple * 2  # Repeat the tuple
print("Repeated tuple:", repeated_tuple)

# Tuple methods
print("\nTuple Methods:")
print("Count of 20 in tuple:", my_tuple.count(20))  # Count occurrences
print("Index of 30 in tuple:", my_tuple.index(30))  # Find index of a value

# Unpacking tuples
print("\nUnpacking Tuples:")
a, b, c, d, e = my_tuple  # Unpacking the tuple into variables
print("Unpacked values:", a, b, c, d, e)

# Nesting tuples
nested_tuple = (my_tuple, another_tuple)
print("\nNested Tuple:", nested_tuple)

# Membership tests
print("\nMembership Tests:")
print("Is 20 in the tuple?", 20 in my_tuple)  # Check membership
print("Is 100 not in the tuple?", 100 not in my_tuple)

# Immutable property of tuples
print("\nImmutability:")
try:
    my_tuple[0] = 99  # Attempt to modify an element
except TypeError as e:
    print("Error:", e)

# Tuple comprehension using generator expressions
print("\nTuple Comprehension (via Generator):")
squared_tuple = tuple(x ** 2 for x in my_tuple)
print("Squares of elements:", squared_tuple)

