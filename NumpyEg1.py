# You can create NumPy arrays using numpy.array() or using functions like numpy.zeros(), numpy.ones(), numpy.arange(), etc.
import numpy as np

# Creating a 1D array
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr_1d)

# Creating a 2D array (Matrix)
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
print("2D Array:\n", arr_2d)

# Creating an array of zeros
arr_zeros = np.zeros((2, 3))  # 2x3 array of zeros
print("Zeros Array:\n", arr_zeros)

# Creating an array of ones
arr_ones = np.ones((3, 2))  # 3x2 array of ones
print("Ones Array:\n", arr_ones)

# Creating an array with a range of numbers
arr_range = np.arange(0, 10, 2)  # Numbers from 0 to 10 with a step of 2
print("Range Array:", arr_range)


#numpy2

# You can reshape NumPy arrays to change their dimensions without changing the underlying data.
# Reshaping a 1D array into a 2D array
import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5, 6])

arr_reshaped = arr_1d.reshape(2, 3)
print("Reshaped Array:\n", arr_reshaped)

# Output:
# Reshaped Array:
# [[1 2 3]
# [4 5 6]]





#numpy3

# NumPy supports multiple data types (e.g., int, float, complex), and you can specify the data type when creating arrays.
# Creating an array with a specific data type
import numpy as np
arr = np.array([1, 2, 3])  #Checking the Data Type
print("Array: ", arr, "Data Type: ", arr.dtype) # Output: int64 (on most 64-bit systems)
arr2 = np.array([1, 'hello', True], dtype=object)
print("Array: ", arr2, "Data Type: ", arr2.dtype)  # object

arr_float = np.array([1, 2, 3, 4], dtype=np.float32)
print("Array with Float DataType:", arr_float)

# Create a complex number array with a specific data type
complex_arr_dtype = np.array([1 + 2j, 3 + 4j, 5 + 6j], dtype=np.complex64)
print("\nComplex Number Array with dtype:", complex_arr_dtype)

# Create a complex number array
complex_arr = np.array([1 + 2j, 3 + 4j, 5 + 6j])
print("\nComplex Number Array:", complex_arr)
print("Data type of the array:", complex_arr.dtype)





#numpy4

# NumPy supports converting data types 
# You can define a custom dtype with multiple fields, similar to structs in C
import numpy as np
arr = np.array([1.1, 2.2, 3.3])
print("Array: ", arr, "Data Type: ", arr.dtype) # float64

# Convert to integer
arr_int = arr.astype(np.int32)
print("Array as Integer: ", arr_int, "Data Type: ", arr_int.dtype)   # int32

# Define a structured data type
person_dtype = np.dtype([('name', 'S10'), ('age', 'i4'), ('weight', 'f4')])

# Create array
people = np.array([
    ('Alice', 25, 55.0),
    ('Bob', 30, 72.5)
], dtype=person_dtype)

print(people[0])         # ('Alice', 25, 55.0)
print(people['name'])    # [b'Alice' b'Bob']

decoded_names = [name.decode('utf-8') for name in people['name']]
print(decoded_names)     # ['Alice', 'Bob']




#numpy5
# NumPy supports element-wise operations such as addition, subtraction,
# multiplication, and division, which can be applied to arrays directly
# without the need for loops.
import numpy as np

# Element-wise addition
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result_add = arr1 + arr2
print("Addition Result:", result_add) # Addition Result: [5 7 9]

# Element-wise multiplication
result_multiply = arr1 * arr2
print("Multiplication Result:", result_multiply) # Multiplication Result: [ 4 10 18]

# Scalar operations (operation with a constant)
result_scalar_add = arr1 + 10
print("Scalar Addition Result:", result_scalar_add) # Scalar Addition Result: [11 12 13]





#numpy6


# You can access individual elements of a NumPy array using indices.
# NumPy supports both 1D and 2D array indexing.
import numpy as np

# 1D Array Indexing
arr = np.array([10, 20, 30, 40, 50])
print("Element at index 2:", arr[2])  # Element at index 2: 30

# 2D Array Indexing
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Element at row 1, column 2:", arr_2d[1, 2])  # Element at row 1, column 2: 6

# Slicing in 1D Array
arr_slice = arr[1:4]  # Extract elements from index 1 to 3
print("Sliced Array:", arr_slice) # Sliced Array: [20 30 40]

# Slicing in 2D Array
arr_2d_slice = arr_2d[0:2, 1:3]  # Extract rows 0 to 1, columns 1 to 2
print("2D Sliced Array:\n", arr_2d_slice)
# 2D Sliced Array:
# [[2 3]
# [5 6]]
