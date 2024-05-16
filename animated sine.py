import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 100)
line, = ax.plot(x, np.sin(x))  # Initial plot

# Update function for animation
def update(frame):
    line.set_ydata(np.sin(x + frame/10))  # Update y-data based on frame
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=50)

# Show the animated plot
plt.title('Animated Sine Wave')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()