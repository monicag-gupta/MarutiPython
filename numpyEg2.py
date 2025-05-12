import numpy as np
# 1D Array:
arr = np.array([1, 2, 3, 4, 5])
print("1D Array by np.array([1, 2, 3, 4, 5]) : "); print(arr)
# 2D Array:
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array by np.array([[1, 2, 3], [4, 5, 6]]) : "); print(arr)
# Zeros and Ones:
zeros = np.zeros((3, 3))
print("Zeros by np.zeros((3, 3)) : "); print(zeros)
ones = np.ones((2, 4))
print("Ones by np.ones((2, 4)) : "); print(ones)
# Empty and Full:
empty = np.empty((2, 2))
print("Empty by np.empty((2, 2)) : "); print(empty)
full = np.full((2, 2), 7)
print("Full by np.full((2, 2), 7) : "); print(full)
# Arange and Linspace:
arr = np.arange(0, 10, 2)  # Array from 0 to 10 with step 2
lin = np.linspace(0, 1, 5)  # 5 evenly spaced numbers from 0 to 1
print("Array from 0 to 10 with step 2 by np.arange(0, 10, 2) : "); print(arr)
print("5 evenly spaced numbers from 0 to 1 by np.linspace(0, 1, 5) : "); print(lin)
# Array Operations: Basic Arithmetic:
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Array Addition: np.array([1, 2, 3]) + np.array([4, 5, 6]) : "); print(a + b)  # Addition
print("Array Multiplication: np.array([1, 2, 3]) * np.array([4, 5, 6]) : "); print(a * b)  # Element-wise multiplication
print("Array Division: np.array([1, 2, 3]) / np.array([4, 5, 6]) : "); print(a / b)  # Element-wise division
# Universal Functions (ufuncs):
print("Array Square root : np.sqrt(np.array([1, 2, 3])) : "); print(np.sqrt(a))  # Square root
print("Array Exponential : np.exp(np.array([1, 2, 3])) : "); print(np.exp(a))   # Exponential
print("Array Exponential : np.sin(np.array([1, 2, 3])) : "); print(np.sin(a))   # Sine
# Matrix Multiplication:
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("Array Multiplication : np.dot(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])) : ")
print(np.dot(a, b))  # Matrix multiplication
# Broadcasting:
a = np.array([1, 2, 3])
b = np.array([[4], [5], [6]])
print("Broadcasting Addition: np.array([1, 2, 3]) + np.array([[4], [5], [6]]) : "); print(a + b)  # Broadcasting addition
# Aggregation Functions:
a = np.array([[1, 2, 3], [4, 5, 6]])
print("Sum of all elements of: np.array([[1, 2, 3], [4, 5, 6]]): \n", np.sum(a))      # Sum of all elements
print("Sum of columns of: np.array([[1, 2, 3], [4, 5, 6]]): \n", np.sum(a, axis=0))  # Sum along columns
print("Mean of: np.array([[1, 2, 3], [4, 5, 6]]): "); print(np.mean(a))     # Mean
print("Max of: np.array([[1, 2, 3], [4, 5, 6]]): "); print(np.max(a))      # Maximum
print("Min of: np.array([[1, 2, 3], [4, 5, 6]]): "); print(np.min(a))      # Minimum
# Reshaping Arrays:
a = np.array([[1, 2, 3], [4, 5, 6]])
print("Reshape to 3X2: np.array([[1, 2, 3], [4, 5, 6]]).reshape((3, 2)): \n", a.reshape((3, 2)))  # Reshape to 3x2 array
print("\nnumpy Examples ends")

