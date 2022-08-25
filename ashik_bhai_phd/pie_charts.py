import matplotlib.pyplot as plt
import numpy as np

plt.style.use("fivethirtyeight")

# understand pie chart

######## --------- Example - 1 ###################

# slices = [60,40]
# labels = ['Sixty', 'Forty']

# plt.pie(slices, labels=labels, wedgeprops={'edgecolor': 'black'})


###############  example - 2

languages_labels = ['JavaScript', 'HTML/CSS', 'Python', 'SQL', 'Java', 'Node.js', 'TypeScript', 'C#', 'Bash/Shell', 'C++', 'PHP', 'C', 'PowerShell', 'Go', 'Kotlin']
slices = [53587, 46259, 39792, 38835, 29162, 27975, 24909, 22984, 22385, 20057, 18130, 17329, 8871, 7879, 6866]

# plt.pie(slices, labels=languages_labels, wedgeprops={'edgecolor': 'black'})

# other properties/attributes

################ Example - 3

# explode
# shadow = True, looking 3-d
# startangle = 90 , degree
# autopct = '%1.1f%%'   '%1.1f%%'

explode = [0,0,0,0.1, 0]

s = slices[:5]
l = languages_labels[:5]

plt.pie(slices[:5], labels=languages_labels[:5], explode=explode, shadow=True, startangle=90, autopct='%1.2f%%', wedgeprops={'edgecolor' : 'black'})

# plt.pie(s, labels=l, explode=explode, shadow=True, startangle=90,
        # autopct='%1.2f%%', wedgeprops={'edgecolor' : 'black'})

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()