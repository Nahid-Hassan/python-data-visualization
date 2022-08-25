import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

ages_x = np.arange(25, 36)

dev_y = [38943, 42424, 46234, 48234,53523, 56000, 62344,64424,67239,69324,76234]

# plt.plot(ages_x, dev_y, color="#444434", label="All Devs")
plt.bar(ages_x, dev_y, color="#444434", label="All Devs")
# plt.barh(ages_x, dev_y, color="#444434", label="All Devs")

dev_py = [39943, 44424, 48234, 52234,59523, 59000, 65344,69424,72239,79324,86234]
plt.bar(ages_x, dev_py, color="#ff4434", label="Python Devs")

dev_js = [38943, 42424, 45234, 51234,54523, 55000, 60344,62424,64239,69324,70234]
plt.bar(ages_x, dev_js, color="#3ffda3", label="JavaScript Developer")

plt.legend()

plt.title("Median Salary (USD) by Age".title())
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

plt.show()