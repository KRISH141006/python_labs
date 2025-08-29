import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([4, 5, 6, 7, 8])

common_values = np.intersect1d(array1, array2)

print("Array 1:", array1)
print("Array 2:", array2)
print("Common values:", common_values)
