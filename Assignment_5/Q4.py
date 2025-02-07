

import numpy as np
import matplotlib.pyplot as plt

# Q4. Generate x values using np.linspace() from -10 to 10 with 100 points
x = np.linspace(-10, 10, 100)

# Use each function from the list below and compute y values using NumPy
# Y = x^2
y1 = x ** 2

# Y = sin(x)
y2 = np.sin(x)

# Y = e^x
y3 = np.exp(x)

# Y = log(|x| + 1)
y4 = np.log(np.abs(x) + 1)

# Plot the chosen function using Matplotlib
plt.figure(figsize=(10, 6))

# Plot Y = x^2
plt.plot(x, y1, label="Y = x^2")

# Add title, labels, and grid for clarity
plt.title("Plot of Y = x^2")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.legend()
plt.show()