import numpy as np
from Farm import Farm
import matplotlib.pyplot as plt
import seaborn as sns
from TransMatrix import *
import random

# seed random numbers for reproducible results
random.seed(1)

hives = [(25, 25)]
dims = 50
size = 4500
trans_mat = transmat_moderate(dims)
#problem = Farm(dims, hives, size, .2, trans_mat)
#x = problem.pollinateRandWalk(200, 10)


problem2 = Farm(dims, hives, size, .23, trans_mat)
problem2.pollinateRandWalk_2(24,10)
print(np.sum(problem2.pmelons))

ax = sns.heatmap(problem2.pmelons, cmap='coolwarm', annot=False, linewidths=0,
                 xticklabels=False, yticklabels=False, square=True, vmax=10,
                 vmin=0)

ax.set_title("Pollinated Watermelons per Square")
plt.show(ax)

#acre = Farm(60,[(30, 30)],9000,0.23,transmat_mat)
