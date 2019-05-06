# Python code for 2D random walk.
import numpy as np
import matplotlib.pyplot as plt
import random


# function to simulate a random walk of n bees through a dim1 by dim2 field
# starting at position (x, y)
def random_walk(x,y,dim1,dim2,steps,bees):

    # matrix tracking number of visits to each square
    visits = np.zeros([dim1,dim2])

    # for each bee loop through n steps, adding to visit matrix
    for i in range(bees):

        matrix = np.zeros([dim1,dim2]) # empty matrix tracking bee's visits
        pos = (x,y)  # starting position
        matrix[pos[0],pos[1]] = 1  # add a visit to starting position

        # loop through each step
        for i in range(steps-1):

            val = random.randint(1,4)  # random value (to determine move)

            # 1, 2, 3, 4 correspond to moving up, down, right or left
            # each move increments the visits to that square by that bee
            if val == 1:
                if (pos[1] + 1) >= dim2:
                    matrix[pos[0],pos[1]] = matrix[pos[0],pos[1]] + 1
                else:
                    matrix[pos[0]][pos[1]+1] = matrix[pos[0]][pos[1]+1] + 1
                    pos = (pos[0],pos[1]+1)
            elif val == 2:
                if (pos[0] + 1) >= dim1:
                    matrix[pos[0],pos[1]] = matrix[pos[0],pos[1]] + 1
                else:
                    matrix[pos[0]+1][pos[1]] = matrix[pos[0]+1][pos[1]] + 1
                    pos = (pos[0]+1,pos[1])
            elif val == 3:
                if (pos[1] - 1) < 0:
                    matrix[pos[0],pos[1]] = matrix[pos[0],pos[1]] + 1
                else:
                    matrix[pos[0]][pos[1]-1] = matrix[pos[0]][pos[1]-1] + 1
                    pos = (pos[0],pos[1]-1)
            else:
                if (pos[0] - 1) < 0:
                    matrix[pos[0],pos[1]] = matrix[pos[0],pos[1]] + 1
                else:
                    matrix[pos[0]-1][pos[1]] = matrix[pos[0]-1][pos[1]] + 1
                    pos = (pos[0]-1,pos[1])

        # print(matrix.sum())  # sanity check (should be num bees every time)
        visits = np.add(visits,matrix)  # add this bee's visits to overall
        visits = visits.astype("int")

    # returns overall visits by the bees
    return visits


# visits = random_walk(5,5,10,10,10,10)
# print(visits)
# print(np.sum(visits))  # sanity check (should be bees * steps)


# function to simulate a random walk of n bees through a dim1 by dim2 field
# starting at position (x, y)
def random_walk_2(x,y,dim1,dim2,steps,bees):

    # matrix tracking number of visits to each square
    visits = np.zeros([dim1,dim2])

    # for each bee loop through n steps, adding to visit matrix
    for i in range(bees):

        matrix = np.zeros([dim1,dim2]) # empty matrix tracking bee's visits
        pos = (x,y)  # starting position
        matrix[pos[0],pos[1]] = 1  # add a visit to starting position

        # loop through each step
        for i in range(steps-1):

            val = random.randint(1,9)  # random value (to determine move)

            # 1, 2, 3, 4 correspond to moving up, down, right or left
            # each move increments the visits to that square by that bee
            if val == 1:
                if (pos[1] + 1) >= dim2:
                    matrix[pos[0],pos[1]] = matrix[pos[0],pos[1]] + 1
                else:
                    matrix[pos[0]][pos[1]+1] = matrix[pos[0]][pos[1]+1] + 1
                    pos = (pos[0],pos[1]+1)
            elif val == 2:
                if (pos[0] + 1) >= dim1:
                    matrix[pos[0],pos[1]] = matrix[pos[0],pos[1]] + 1
                else:
                    matrix[pos[0]+1][pos[1]] = matrix[pos[0]+1][pos[1]] + 1
                    pos = (pos[0]+1,pos[1])
            elif val == 3:
                if (pos[1] - 1) < 0:
                    matrix[pos[0],pos[1]] = matrix[pos[0],pos[1]] + 1
                else:
                    matrix[pos[0]][pos[1]-1] = matrix[pos[0]][pos[1]-1] + 1
                    pos = (pos[0],pos[1]-1)
            elif val == 4:
                if (pos[0] - 1) < 0:
                    matrix[pos[0],pos[1]] = matrix[pos[0],pos[1]] + 1
                else:
                    matrix[pos[0]-1][pos[1]] = matrix[pos[0]-1][pos[1]] + 1
                    pos = (pos[0]-1,pos[1])
            elif val == 5:
                if (pos[1] + 1) >= dim1 or (pos[0] + 1) >= dim0:
                    matrix[pos[0],pos[1]] = matrix[pos[0],pos[1]] + 1
                else:
                    matrix[pos[0]+1][pos[1]+1] = matrix[pos[0]+1][pos[1]+1] + 1
                    pos = (pos[0]+1,pos[1]+1)
            elif val == 6:
                if (pos[1] - 1) < 0 or (pos[0] + 1) >= dim0:
                    matrix[pos[0],pos[1]] = matrix[pos[0],pos[1]] + 1
                else:
                    matrix[pos[0]-1][pos[1]+1] = matrix[pos[0]-1][pos[1]+1] + 1
                    pos = (pos[0]-1,pos[1]+1)
            elif val == 7:
                if (pos[1] + 1) >= dim1 or (pos[0] - 1) < 0:
                    matrix[pos[0],pos[1]] = matrix[pos[0],pos[1]] + 1
                else:
                    matrix[pos[0]+1][pos[1]-1] = matrix[pos[0]+1][pos[1]-1] + 1
                    pos = (pos[0]+1,pos[1]-1)
            elif val == 8:
                if (pos[1] - 1) < 0 or (pos[0] - 1) < 0:
                    matrix[pos[0],pos[1]] = matrix[pos[0],pos[1]] + 1
                else:
                    matrix[pos[0]-1][pos[1]-1] = matrix[pos[0]-1][pos[1]-1] + 1
                    pos = (pos[0]-1,pos[1]-1)
            else:
                matrix[pos[0],pos[1]] = matrix[pos[0],pos[1]] + 1

        # print(matrix.sum())  # sanity check (should be num bees every time)
        visits = np.add(visits,matrix)  # add this bee's visits to overall
        visits = visits.astype("int")

    # returns overall visits by the bees
    return visits
