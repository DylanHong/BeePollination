import numpy as np
from Farm import Farm
import matplotlib.pyplot as plt
import seaborn as sns
from TransMatrix import *

hives = [(3, 3), (15, 15)]
dims = 20
size = 3000
trans_mat = transmat_simple(dims)
problem = Farm(dims, hives, size, .2, trans_mat)
x = problem.pollinateRandWalk(30, 5)
print(x)


problem2 = Farm(dims, hives, size, .2, trans_mat)
problem2.pollinateSeason(30, 5)

ax = sns.heatmap(problem2.pmelons, cmap='RdBu_r', annot=True, linewidths=.5)
plt.show(ax)
