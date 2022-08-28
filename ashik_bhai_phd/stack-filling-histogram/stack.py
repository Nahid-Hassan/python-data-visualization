import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-deep')

minutes = np.arange(1, 10)  # 1...9

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

# stackplot(x, list, list ..., [colors=, [labels=,)
# plt.stackplot(minutes, player1, player2, player3)
labels = ['Player 1', 'Player 2', 'Player 3']
# plt.stackplot(minutes, player1, player2, player3, labels=labels)


dev1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
dev2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
dev3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

dev_labels = ['Dev 1', 'Dev 2', 'Dev 3']

plt.stackplot(minutes, dev1, dev2, dev3, labels=dev_labels)

# for labels
# plt.legend(loc="upper left") # upper lower left right
plt.legend(loc=(.05, .7))  # upper lower left right


plt.title("My Awesome Stack Plot")
plt.tight_layout()

plt.grid(alpha=.3)
plt.show()
