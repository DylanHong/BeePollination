import numpy as np

class Farm:

    def __init__(self, dims, locations, hive_size, pollination_rate, trans_mat):
        self.dims = dims
        self.locs = locations
        self.num_hives = len(locations)

        self.hive_size = hive_size
        self.pr = pollination_rate  # pollination rate

        self.field = np.zeros([dims, dims])

        self.transition = trans_mat  # transition matrix for bees

        for loc in self.locs:
            self.field[loc[0], loc[1]] = hive_size


hives = [(0, 0), (3, 0)]
dims = 4
size = 100
trans_mat = np.zeros([dims**2, dims**2])

problem = Farm(dims, hives, size, .5, trans_mat)

print(problem.field)
print(problem.transition)
