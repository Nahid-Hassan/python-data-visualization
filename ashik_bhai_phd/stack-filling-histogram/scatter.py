import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

# randint(low, [high, size)
x = np.random.randint(10, 100, size=25)
y = np.random.randint(10, 100, size=25)

colors = np.random.randint(10, 100, size=25)


# plt.scatter(x, y)
# plt.scatter(x, y, c='green', edgecolor='black', linewidth=1)
plt.scatter(x, y, s=100, c=colors, cmap='Greens', edgecolor='black', linewidth=1)

cbar = plt.colorbar()
cbar.set_label('Satisfaction')

plt.show()
