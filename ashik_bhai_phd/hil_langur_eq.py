# wiki     : https://en.wikipedia.org/wiki/Hill_equation_(biochemistry)
# mathtext : https://matplotlib.org/stable/tutorials/text/mathtext.html

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-deep')

# #################### Generate Indexes #################
k_a = 1e-06
c = np.linspace(0, 2, 200)
d, c = c.copy(), c * 1e-06

# ################## Calculation #################
thita_n_point_2 = ((c / k_a) ** .2) / ((1 + ((c / k_a)) ** .2)) 
thita_n_point_5 = ((c / k_a) ** .5) / ((1 + ((c / k_a)) ** .5))
thita_n_1 = (c / k_a) / (1 + (c / k_a))
thita_n_2 = ((c / k_a) ** 2) / ((1 + ((c / k_a)) ** 2)) 
thita_n_4 = ((c / k_a) ** 4) / ((1 + ((c / k_a)) ** 4)) 


# ################## Plotting ##############
plt.plot(d, thita_n_point_2 , label='n = .2', marker='.', markevery=20)
plt.plot(d, thita_n_point_5 , label='n = .5', marker='.', markevery=20)
plt.plot(d, thita_n_1, label='n = 1', marker='.', markevery=20)
plt.plot(d, thita_n_2, label='n = 2', marker='.', markevery=20)
plt.plot(d, thita_n_4, label='n = 4', marker='.', markevery=20)


########### ----------- Text --------------- ###############
text_kwargs = dict(ha='center', va='center', fontsize=16)

# lower left (0, 0)
# upper right (1, 1)
plt.text(.8, .8, r"$\theta = \frac{(c / k_a)^n}{1 + (c / k_a)^n}$",  bbox=dict(facecolor='white', alpha=.8), **text_kwargs)


# ############## Customizing Plot ##############
plt.legend()
plt.grid(alpha=.1)
plt.title("Hypothetical Hill-Langmuir Curves")
plt.ylabel(r"$\theta$")
plt.xlabel(r"$c(\mu M)$")

plt.show()

