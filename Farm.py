import numpy as np
from TransMatrix import *

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

        # updates field to reflect hive locations (at start)
        for loc in self.locs:
            self.field[loc[0], loc[1]] = hive_size

# some test code
hives = [(0, 0), (3, 0)]
dims = 4
size = 100
trans_mat = transmat_simple(dims)
problem = Farm(dims, hives, size, .5, trans_mat)

print(problem.field)
print(problem.transition)
