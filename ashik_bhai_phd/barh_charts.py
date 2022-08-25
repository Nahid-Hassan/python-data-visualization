import matplotlib.pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

languages = ["Assembly", 'Go', 'Ruby', 'Others', 'C', 'TypeScript', 'C++', 'PHP', 'C#',
             "Bash", "Java", 'Python', "SQL", 'HTML/CSS', 'JavaScript']

popularity = [8344,12342, 12342, 13000, 19000, 20000, 23432, 25423, 27324,32342,35432,37242,
              47243, 55324,58324]

# languages.reverse()
# popularity.reverse()

# plt.bar(languages, popularity)
plt.barh(languages, popularity)
plt.show()