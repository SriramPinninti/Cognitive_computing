


import numpy as np
import matplotlib.pyplot as plt

# Q.2 (b) For the array: array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0]), find
array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])

# i. Integer elements only
integer_elements = array[array == array.astype(int)]
print("Integer elements only:", integer_elements)

# ii. Float elements only
float_elements = array[array != array.astype(int)]
print("Float elements only:", float_elements)

