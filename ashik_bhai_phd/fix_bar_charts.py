import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

ages_x = np.arange(25, 36)

x_indexes = np.arange(len(ages_x))

print(x_indexes)

width = .25

dev_y = [38943, 42424, 46234, 48234,53523, 56000, 62344,64424,67239,69324,76234]

plt.bar(x_indexes - width, dev_y, width = width, label="All Devs")

dev_py = [39943, 44424, 48234, 52234,59523, 59000, 65344,69424,72239,79324,86234]
plt.bar(x_indexes, dev_py, width = width, label="Python Devs")

dev_js = [38943, 42424, 45234, 51234,54523, 55000, 60344,62424,64239,69324,70234]
plt.bar(x_indexes + width, dev_js, width = width, label="JavaScript Developer")
# plt.bar(x_indexes + 2 * width, dev_js, width = width, label="JavaScript Developer")

plt.legend()

plt.xticks(ticks=x_indexes, labels=ages_x)

plt.title("Median Salary (USD) by Age".title())
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

plt.show()