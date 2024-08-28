import matplotlib.pyplot as plt
import numpy as np

# Define more complex data
# This creates three datasets (x1, y1), (x2, y2), and (x3, y3)
x1 = np.linspace(0.0, 5.0, 100)  # Creates 100 points between 0 and 5
y1 = np.sin(2*np.pi*x1)  # Sine wave function

x2 = np.random.rand(50)  # 50 random points between 0 and 1
y2 = x2**2  # Square these points

x3 = np.linspace(2.0, 8.0, 200)
y3 = np.exp(x3)  # Exponential function

# Create the plot
plt.plot(x1, y1, label='Sine Wave')  # Plot with label
plt.plot(x2, y2, 'o', label='Random Points Squared')  # Plot with marker and label
plt.plot(x3, y3, '--', label='Exponential Curve')  # Plot with linestyle and label

# Add legend to identify each dataset
plt.legend()

# Customize labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Complex Line Plot')

# Improve plot appearance (optional)
plt.grid(True)  # Add grid lines

# Show the plot
plt.show()