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






#numpy7

# Boolean indexing allows you to access array elements based on a condition.
import numpy as np

# Boolean indexing
arr = np.array([10, 20, 30, 40, 50])
condition = arr > 25
print("Array: ", arr) # Array:  [10 20 30 40 50]
print("Boolean Indexed Array:", arr[condition])
# Boolean Indexed Array: [30 40 50]
arr2 = arr[condition]
print("Array Arr2:", arr2) # Array Arr2: [30 40 50]
print("Original Array: ", arr) # Original Array:  [10 20 30 40 50]





#numpy8

# Universal Functions (ufuncs): NumPy provides vectorized functions (ufuncs)
# that can be applied element-wise to arrays.
import numpy as np
# Square root of each element
arr = np.array([1, 4, 9, 16])
result_sqrt = np.sqrt(arr)
print("Square Root of Array:", result_sqrt) 
# Exponentiation (e^x) of each element
result_exp = np.exp(arr)
print("\nExponentiation of Array:", result_exp)

# Matrix Operations:
# NumPy provides a range of matrix operations, including matrix multiplication and transpose.
# Matrix Transpose
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
arr_transpose = arr_2d.T  # Transpose of the matrix
print("\nTransposed Matrix:\n", arr_transpose)
# Matrix multiplication
arr_2d_1 = np.array([[1, 2], [3, 4]])
arr_2d_2 = np.array([[5, 6], [7, 8]])
arr_multiply = np.dot(arr_2d_1, arr_2d_2)
print("Matrix Multiplication:\n", arr_multiply)





#numpy9

# NumPy allows performing various operations on complex number arrays. # Some of these operations include addition, subtraction, multiplication, # and accessing real and imaginary parts of the complex numbers.
# Arithmetic Operations with Complex Numbers # Perform arithmetic operations on complex numbers
import numpy as np
arr1 = np.array([1 + 2j, 3 + 4j, 5 + 6j])
arr2 = np.array([2 + 3j, 4 + 5j, 6 + 7j])
# Addition
result_add = arr1 + arr2
print("\nAddition of complex arrays:", result_add)
# Subtraction
result_subtract = arr1 - arr2
print("\nSubtraction of complex arrays:", result_subtract) 
# Multiplication
result_multiply = arr1 * arr2
print("\nMultiplication of complex arrays:", result_multiply)
# Division
result_divide = arr1 / arr2
print("\nDivision of complex arrays:", result_divide)
# Accessing Real and Imaginary Parts of Complex Numbers
# You can access the real and imaginary parts of complex numbers using .real and .imag.
real_part = arr1.real
imaginary_part = arr1.imag
print("\nReal part of the complex array:", real_part)
print("Imaginary part of the complex array:", imaginary_part)





#numpy10

import numpy as np

# Generate numbers from 0 to 9 with step 1
arr1 = np.arange(0, 10, 1)
print("arange example:", arr1) # arange example: [0 1 2 3 4 5 6 7 8 9]

# Generate numbers from 1 to 10 with step 2
arr2 = np.arange(1, 10, 2)
print("arange with step:", arr2) # arange with step: [1 3 5 7 9]

# Generate 5 numbers between 0 and 1
arr1 = np.linspace(0, 1, 5)
print("linspace example:", arr1)  # linspace example: [0.   0.25 0.5  0.75 1.  ]

# Generate 5 numbers between 0 and 1, excluding the endpoint
arr2 = np.linspace(0, 1, 5, endpoint=False)
print("linspace without endpoint:", arr2) # linspace without endpoint: [0.  0.2 0.4 0.6 0.8]

# Generate 5 numbers and return the step size
arr3, step = np.linspace(0, 10, 5, retstep=True)
print("linspace with step size:", arr3, ", step:", step) 
# linspace with step size: [ 0.  2.5  5.  7.5 10. ] , step: 2.5





