import numpy as np
from Farm import Farm
import matplotlib.pyplot as plt
import seaborn as sns
from TransMatrix import *

hives = [(20, 15), (80, 70)]
dims = 100
size = 3000
trans_mat = transmat_simple(dims)
problem = Farm(dims, hives, size, .2, trans_mat)
x = problem.pollinateRandWalk(200, 10)


problem2 = Farm(dims, hives, size, .2, trans_mat)
problem2.pollinateRandWalk_2(30, 5)

ax = sns.heatmap(problem2.pmelons, cmap='RdBu_r', annot=False, linewidths=0,
                 xticklabels=False, yticklabels=False, square=True)

ax.set_title("Pollinated Watermelons per Square")
plt.show(ax)
