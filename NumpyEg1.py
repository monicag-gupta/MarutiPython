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
