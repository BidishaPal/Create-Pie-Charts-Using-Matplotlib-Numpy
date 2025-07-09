import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Mango", "Oranges"]
mycolors = ["red", "yellow", "green", "#f58442"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()
