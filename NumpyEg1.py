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

