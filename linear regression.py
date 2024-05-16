import matplotlib.pyplot as plt
import numpy as np

#data
y=np.array([4,7,5,7,9,5])
x=np.array([7,6,6,8,6,5])

#reg fit
slope, intersept=np.polyfit(x,y,1)

#line
line=slope*x+intersept

#scatter points
plt.scatter(x,y,c='b')

#plot reg line
plt.plot(x,line,label='reg line',c='r')

#add labels
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')

#display
plt.show()