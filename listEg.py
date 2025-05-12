# List declaration
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

# Properties of lists
print("\nProperties:")
print("Length of list:", len(my_list))  # Length of the list
print("Minimum value in the list:", min(my_list))  # Minimum value
print("Maximum value in the list:", max(my_list))  # Maximum value
print("Sum of all elements in the list:", sum(my_list))  # Sum of elements

# Operations on lists
print("\nOperations:")
my_list.append(60)  # Append an element
print("After appending 60:", my_list)

my_list.extend([70, 80])  # Extend the list
print("After extending with [70, 80]:", my_list)

my_list.insert(2, 25)  # Insert at a specific position
print("After inserting 25 at index 2:", my_list)

popped_value = my_list.pop(3)  # Pop an element at index 3
print("After popping value at index 3:", my_list)
print("Popped value:", popped_value)

my_list.remove(25)  # Remove the first occurrence of a value
print("After removing 25:", my_list)

print("Index of 40:", my_list.index(40))  # Find index of an element

print("Count of 40:", my_list.count(40))  # Count occurrences of a value

my_list.reverse()  # Reverse the list
print("After reversing the list:", my_list)

my_list.sort()  # Sort the list
print("After sorting the list:", my_list)

# List slicing
print("\nSlicing:")
print("First three elements:", my_list[:3])
print("Elements from index 2 to 5:", my_list[2:5])
print("Last three elements:", my_list[-3:])

# List concatenation and repetition
print("\nConcatenation and Repetition:")
another_list = [100, 200]
concatenated_list = my_list + another_list  # Concatenate two lists
print("Concatenated list:", concatenated_list)

repeated_list = my_list * 2  # Repeat the list
print("Repeated list:", repeated_list)

# List comprehension
print("\nList Comprehension:")
squared_list = [x ** 2 for x in my_list]
print("Squares of elements:", squared_list)

# Copying a list
print("\nCopying:")
copied_list = my_list.copy()  # Copy the list
print("Copied list:", copied_list)

# Clearing a list
my_list.clear()  # Clear all elements
print("After clearing the list:", my_list)

