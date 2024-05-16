import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# random 2D data 
data = np.random.rand(10, 10)

# heatmap using Seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(data, annot=True, cmap='viridis')
plt.title('Heatmap of 2D Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()