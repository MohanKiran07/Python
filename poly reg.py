import matplotlib.pyplot as plt
import numpy as np

#data
x=np.array([1,2,3,4,5])
y=np.array([1,10,9,10,13])

#ploy fit
poly=np.poly1d(np.polyfit(x,y,2))

#y val of ploy fit
y_fit=poly(x)

#scatter points
plt.scatter(x,y,c='b')

#plot reg line
plt.plot(x,y_fit,label='poly reg',c='r')

#add labels
plt.xlabel('X')
plt.ylabel('Y')
plt.title('polynomial Regression')

#display
plt.show()