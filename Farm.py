import numpy as np

class Farm:

    def __init__(self, dims, locations, hive_size, pollination_rate):
        self.dims = dims
        self.locs = locations
        self.num_hives = len(locations)

        self.hive_size = hive_size
        self.pr = pollination  # pollination rate

        self.field = np.zeros([dims, dims])

        for loc in self.locs:
            self.field[loc[0], loc[1]] = hive_size


hives = [(0, 0), (3, 0)]
dims = 4
size = 100

problem = Farm(dims, hives, size)

print(problem.field)
