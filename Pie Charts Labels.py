import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Oranges", "Mango"]

plt.pie(y, labels = mylabels)
plt.show() 
