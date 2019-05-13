import numpy as np
from TransMatrix import *
import matplotlib.pyplot as plt
import seaborn as sns
import operator
from RandomWalk import random_walk, random_walk_2
import random


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

        self.mps = 10.0

        self.melons = np.full((dims,dims), self.mps)
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
            self.pmelons = np.ceil(self.pmelons)

            # remove pollinated melons from melons
            self.melons = np.full((self.dims,self.dims), self.mps)

            self.melons -= self.pmelons

    def pollinateSeason(self,steps,days):
        for i in range(days):
            self.pollinateDay(steps)
            self.field = self.of.copy()

    def pollinateRandWalk(self,steps,days):
        visits = np.zeros((self.dims,self.dims))
        for i in range(days):
            for i in range(self.num_hives):
                x, y = self.locs[i]
                day = random_walk(x,y,self.dims,self.dims,steps,self.hive_size)
                visits = np.add(day, visits)

            # update which melons are pollinated
            self.pmelons += np.minimum(visits,self.melons) * self.pr
            self.pmelons = np.round(self.pmelons)

            # remove pollinated melons from melons
            self.melons = np.full((self.dims,self.dims), self.mps)
            self.melons -= self.pmelons

        return visits

    def pollinateRandWalk_2(self,steps,days):
        visits = np.zeros((self.dims,self.dims))
        for i in range(days):
            for i in range(self.num_hives):
                x, y = self.locs[i]
                day = random_walk_2(x,y,self.dims,self.dims,steps,self.hive_size)
                visits = np.add(day, visits)

            self.pmelons += np.minimum(visits,self.melons) * self.pr

            # if random.random() < 0.5:
            #     self.pmelons = np.ceil(self.pmelons)
            # else:
            #     self.pmelons = np.floor(self.pmelons)


            self.pmelons = np.ceil(self.pmelons)

            # remove pollinated melons from melons
            self.melons = np.full((self.dims,self.dims), self.mps)
            self.melons -= self.pmelons

        return visits


def optimize(dims,size,pr,trans_mat,steps,days):
    totals = {}
    for i in range(dims**2):
        mod = i%dims
        newi = int(i/dims)
        print(mod)
        print(newi)
        curr = Farm(dims,[(newi,mod)],size,pr,trans_mat)
        curr.pollinateSeason(steps,days)
        totals[(newi,mod)] = np.sum(curr.pmelons)

    max_value = max(totals.values())  # maximum value
    max_keys = [k for k, v in totals.items() if v == max_value] # getting all keys containing the `maximum`

    return max_value, max_keys

# # some test code
# hives = [(2, 2)]
# dims = 10
# size = 1000
# trans_mat = transmat_simple(dims)
# problem = Farm(dims, hives, size, .2, trans_mat)
# x = problem.pollinateRandWalk(5,10)
# print(x)
# print(problem.pmelons)
# print(np.sum(problem.pmelons))
#
# print('-------------')
#
# problem2 = Farm(dims, hives, size, .2, trans_mat)
# problem2.pollinateSeason(5,10)
# print(problem2.pmelons)
# print(np.sum(problem2.pmelons))
#
# ax = sns.heatmap(problem.pmelons, cmap='RdBu_r', annot=True, linewidths=.5)
# plt.show(ax)
