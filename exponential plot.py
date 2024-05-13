import numpy as np
import matplotlib.pyplot as plt

#data
x=np.linspace(-5,5,100)

#funtion
a=2
y=np.power(a,x)

#plot
plt.plot(x,y, label=f'{a}^X', c='k')

#add labels
plt.xlabel('X')
plt.ylabel(f'{a}^X')
plt.title(f'plot of {a}^X')
plt.legend()
plt.grid()

#display
plt.show()
