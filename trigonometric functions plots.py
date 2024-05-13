import numpy as np
import matplotlib.pyplot as plt

# random data
x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# trigonometric functions
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)
y_sec = 1 / np.cos(x)
y_cosec = 1 / np.sin(x)
y_cot = 1 / np.tan(x)

# create subplots
fig, ax = plt.subplots(3, 2, figsize=(12, 12))

# sine subplot graph
ax[0, 0].plot(x, y_sin, label='sine', c='r')
ax[0, 0].set_ylabel('sin(x)')
ax[0, 0].set_xlabel('Radians(π)')
ax[0, 0].set_title('Sine')
ax[0, 0].legend()
ax[0, 0].grid()

# cosine subplot graph
ax[0, 1].plot(x, y_cos, label='cos(x)', c='b')
ax[0, 1].set_ylabel('cos(x)')
ax[0, 1].set_xlabel('Radians(π)')
ax[0, 1].set_title('Cosine')
ax[0, 1].legend()
ax[0, 1].grid()

# tan subplot graph
ax[1, 0].plot(x, y_tan, label='tan(x)', c='g')
ax[1, 0].set_ylabel('tan(x)')
ax[1, 0].set_xlabel('Radians(π)')
ax[1, 0].set_title('Tan')
ax[1, 0].legend()
ax[1, 0].grid()

# sec subplot graph
ax[1, 1].plot(x, y_sec, label='sec(x)', c='y')
ax[1, 1].set_ylabel('sec(x)')
ax[1, 1].set_xlabel('Radians(π)')
ax[1, 1].set_title('Sec')
ax[1, 1].legend()
ax[1, 1].grid()

# cosec subplot graph
ax[2, 0].plot(x, y_cosec, label='cosec(x)', c='k')
ax[2, 0].set_ylabel('cosec(x)')
ax[2, 0].set_xlabel('Radians(π)')
ax[2, 0].set_title('Cosec')
ax[2, 0].legend()
ax[2, 0].grid()

# cotan subplot graph
ax[2, 1].plot(x, y_cot, label='cot(x)', c='c')
ax[2, 1].set_ylabel('cot(x)')
ax[2, 1].set_xlabel('Radians(π)')
ax[2, 1].set_title('Cot')
ax[2, 1].legend()
ax[2, 1].grid()

# adjust layout
fig.suptitle("Trigonometric Function Plots")
plt.tight_layout()
plt.show()