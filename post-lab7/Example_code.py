# example codes

# 1

import numpy as np
list1 = [2, 4, 6, 8]
array1 = np.array(list1)
print(array1)

# 2

import numpy as np
array1 = np.array([2, 4, 6, 8])
print(array1)

# 3

import numpy as np
array1 = np.zeros(4)
print(array1)

# 4

import numpy as np
# create an array with values from 0 to 4
array1 = np.arange(5)
print("Using np.arange(5):", array1)
# create an array with values from 1 to 8 with a step of 2
array2 = np.arange(1, 9, 2)
print("Using np.arange(1, 9, 2):",array2)

# 5

import numpy as np
# generate an array of 5 random numbers
array1 = np.random.rand(5)
print(array1)

# 6

import numpy as np
# Example 1: Creation of 1D array
arr1=np.array([10,20,30])
print("My 1D array:\n",arr1)

# 7

import numpy as np
arr2 = np.array([[10,20,30],[40,50,60]])
print("My 2D numpy array:\n", arr2)

# 8

import numpy as np
arr= np.arange(0, 20, 3)
print ("A sequential array with steps of 3:\n", arr)

# 9

import numpy as np
arr= np.linspace(0, 3, 5)
print ("A sequential array with 5 values between 0 and 3:\n", arr)

# 10

import numpy as np
arr = np.ones((2,3))
print("numpy array:\n", arr)
print("Type:", type(arr))

# 11

import numpy as np
# create an array of  integers
int_array = np.array([-3, -1, 0, 1])
# create an array of floating-point numbers
float_array = np.array([0.1, 0.2, 0.3])
# create an array of complex numbers
complex_array = np.array([1+2j, 2+3j, 3+4j])
# check the data type of int_array
print(int_array.dtype)  # prints int64
# check the data type of float_array
print(float_array.dtype)  # prints float64
# check the data type of complex_array
print(complex_array.dtype)  # prints complex128

# 12

import numpy as np
# create an array of 8-bit integers
array1 = np.array([1, 3, 7], dtype='int8')
# create an array of unsigned 16-bit integers
array2 = np.array([2, 4, 6], dtype='uint16')
# create an array of 32-bit floating-point numbers
array3 = np.array([1.2, 2.3, 3.4], dtype='float32')
# create an array of 64-bit complex numbers
array4 = np.array([1+2j, 2+3j, 3+4j], dtype='complex64')
# print the arrays and their data types
print(array1, array1.dtype)
print(array2, array2.dtype)
print(array3, array3.dtype)
print(array4, array4.dtype)

# 13

import numpy as np
# create an array of integers
int_array = np.array([1, 3, 5, 7])
# convert data type of int_array to float
float_array = int_array.astype('float')
# print the arrays and their data types
print(int_array, int_array.dtype)
print(float_array, float_array.dtype)

# 14

import numpy as np
# create a 2-D array 
array1 = np.array([[2, 4, 6],
                  [1, 3, 5]])
# check the dimension of array1
print(array1.ndim)

# 15

import numpy as np
array1 = np.array([[1, 2, 3],
                 [6, 7, 8]])
# return total number of elements in array1
print(array1.size)

# 16

import numpy as np
array1 = np.array([[1, 2, 3],
                [6, 7, 8]])
# return a tuple that gives size of array in each dimension
print(array1.shape)

# 17

import numpy as np
# create an array of integers 
array1 = np.array([6, 7, 8])
# check the data type of array1
print(array1.dtype)

# 18

import numpy as np
# create a default 1-D array of integers
array1 = np.array([6, 7, 8, 10, 13])
# create a 1-D array of 32-bit integers 
array2 = np.array([6, 7, 8, 10, 13], dtype=np.int32)
# use of itemsize to determine size of each array element of array1 and array2
print(array1.itemsize)  # prints 8
print(array2.itemsize)  # prints 4


# 19

import numpy as np
array1 = np.array([6, 7, 8])
array2 = np.array([[1, 2, 3],
                   	    [6, 7, 8]])
# print memory address of array1's and array2's data
print("\nData of array1 is: ",array1.data)
print("Data of array2 is: ",array2.data)

# 20

import numpy as np
p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("Original matrices:")
print(p)
print(q)
# Perform matrix multiplication using np.dot
result1 = np.dot(p, q)
print("Result of the matrix multiplication:")
print(result1)

# 21

import numpy as np
from numpy import linalg as LA
a = np.array([[1, 0], [1, 2]])
# Display the original 2x2 array 'a'
print("Original 2-d array")
print(a)
print("Determinant of the said 2-D array:")
print(np.linalg.det(a))
