import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
path = '/storage/emulated/0/download/data.csv'
dt = pd.read_csv(path)

# Coordinates
x, y = dt['Duration'], dt['Calories']

# Slope and intercept
slope, intercept = np.polyfit(x, y, 1)

# Linear regression line
line = slope * x + intercept

# Scatter plot calories and duration
plt.scatter(x, y, c='b', label='Data Points')

# Plot the regression line
plt.plot(x, line, c='r', label='Linear Regression Line')

# Add labels and title
plt.xlabel('Duration')
plt.ylabel('Calories')
plt.title('Duration vs Calories Linear Regression')

# Show the legend
plt.legend()

# Show the plot
plt.show()