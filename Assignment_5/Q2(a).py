

import numpy as np
import matplotlib.pyplot as plt

# Q.2 (a) For the array: array = np.array([10, 52, 62, 16, 16, 54, 453]), find
array = np.array([10, 52, 62, 16, 16, 54, 453])

# i. Sorted array
sorted_array = np.sort(array)
print("Sorted array:", sorted_array)

# ii. Indices of sorted array

sorted_indices = np.argsort(array)
print("Indices of sorted array:", sorted_indices)

# iii. 4 smallest elements

smallest_elements = np.partition(array, 4)[:4]
print("4 smallest elements:", smallest_elements)

# iv. 5 largest elements

largest_elements = np.partition(array, -5)[-5:]
print("5 largest elements:", largest_elements)



