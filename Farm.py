import numpy as np
from TransMatrix import *
import matplotlib.pyplot as plt
import seaborn as sns
import operator


# class for simulating bee pollination on a farm (modeled as a grid)
class Farm:

    # pass dimensions of farm, hive locations and size, chance of pollination in
    # a timestep, and transition matrix modeling bee movement around the farm
    def __init__(self, dims, locations, hive_size, pollination_rate, trans_mat):
        self.dims = dims  # dimensions
        self.locs = locations  # locations as a list of tuples
        self.num_hives = len(locations)

        self.hive_size = hive_size
        self.pr = pollination_rate  # pollination rate

        self.field = np.zeros([dims, dims])  # array field with bee locations

        self.transition = trans_mat  # transition matrix for bee movement

        self.melons = np.full((dims,dims), 100.0)
        self.pmelons = np.zeros([dims,dims])

        # updates field to reflect hive locations (at start)
        for loc in self.locs:
            self.field[loc[0], loc[1]] = hive_size

        self.of = self.field.copy()

    def timestep(self):
        #field = self.field
        # reshape the matrix for multiplication
        self.field = np.reshape(self.field, (1, self.dims**2))

        # multiply the matrices
        self.field = np.matmul(self.field, self.transition)
        #self.field = np.round(self.field)

        # reshape back to original dimensions
        self.field = np.reshape(self.field, (self.dims,self.dims))

        #return field

    def pollinateDay(self,steps):
        for i in range(steps):
            # update bee locations
            self.timestep()

            # update which melons are pollinated
            self.pmelons += np.minimum(self.field,self.melons) * self.pr
            self.pmelons = np.round(self.pmelons)

            # remove pollinated melons from melons
            self.melons = np.full((dims,dims), 100.0)

            self.melons -= self.pmelons

    def pollinateSeason(self,steps,days):
        for i in range(days):
            self.pollinateDay(steps)
            self.field = self.of.copy()


def optimize(dims,size,.1,trans_mat,steps,days):
    totals = {}
    for i in range(self.dims**2):
        mod = i%dims
        newi = i/dims
        curr = Farm(dims,[(newi,mod)])
        curr.pollinateSeason(steps,days)
        totals[i] = np.sum(curr.pmelons)

    max_value = max(totals.values())  # maximum value
    max_keys = [k for k, v in totals.items() if v == max_value] # getting all keys containing the `maximum`

    return max_value, max_keys

# some test code
hives = [(5, 5)]
dims = 10
size = 1000
trans_mat = transmat_simple(dims)
problem = Farm(dims, hives, size, .1, trans_mat)
problem.pollinateSeason(10,20)

dims = 10
size = 1000
trans_mat = transmat_simple(dims)



# print(problem.pmelons)
# print(problem.melons)
#
# ax = sns.heatmap(problem.pmelons)
# plt.show(ax)
