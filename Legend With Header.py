import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 30, 15, 20])
mylabels = ["Lotus", "Rose", "Sunflower", "Marigold"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Flowers:")
plt.show()
