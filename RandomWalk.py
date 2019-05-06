# Python code for 2D random walk.
import numpy as np
import matplotlib.pyplot as plt
import random

# defining the number of steps
n = 1000

#creating two array for containing x and y coordinate
#of size equals to the number of size and filled up with 0's


#matrix = np.zeros([dim1,dim2])


def move1(x,y,dim1,dim2,steps,bees):
    mastermatrix = np.zeros([dim1,dim2])
    for i in range(bees):
        matrix = np.zeros([dim1,dim2])
        pos = (x,y)
        matrix[pos[0],pos[1]] = 1
        for i in range(steps-1):
            val = random.randint(1,4)
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
                if (pos[1] - 1) <= 0:
                    matrix[pos[0],pos[1]] = matrix[pos[0],pos[1]] + 1
                else:
                    matrix[pos[0]][pos[1]-1] = matrix[pos[0]][pos[1]-1] + 1
                    pos = (pos[0],pos[1]-1)
            else:
                if (pos[0] - 1) <= 0:
                    matrix[pos[0],pos[1]] = matrix[pos[0],pos[1]] + 1
                else:
                    matrix[pos[0]-1][pos[1]] = matrix[pos[0]-1][pos[1]] + 1
                    pos = (pos[0]-1,pos[1])

        print(matrix.sum())
        mastermatrix = np.add(mastermatrix,matrix)
        mastermatrix = mastermatrix.astype("int")
    return mastermatrix


rand = move1(5,5,10,10,10,10)
print(rand)
print(np.sum(rand))





# def move(x,y,steps,dim1,dim2,bees):
#     dayx = np.zeros(steps)
#     dayy = np.zeros(steps)
#
#     matrix = np.zeros([dim1,dim2])
#
#     for i in range(bees):
#         x = np.zeros(steps)
#         y = np.zeros(steps)
#         x[0] = 5
#         y[0] = 5
#         pos = (5,5)
#         for i in range(1,steps):
#             val = random.randint(1,4)
#             if val == 1:
#                 x[i] = x[i - 1] + 1
#                 y[i] = y[i - 1]
#                 matrix[i]
#             elif val == 2:
#                 x[i] = x[i - 1] - 1
#                 y[i] = y[i - 1]
#             elif val == 3:
#                 x[i] = x[i - 1]
#                 y[i] = y[i - 1] + 1
#             else:
#                 x[i] = x[i - 1]
#                 y[i] = y[i - 1] - 1
#         dayx += x
#         dayy += y
#
#     return dayx,dayy
#
#
# rand = move(3,3,100,6,6,10)
# print(rand)
#
# plt.figure(1)
# plt.scatter(rand[0],rand[1])
# plt.show()


# plotting stuff:
# pylab.title("Random Walk ($n = " + str(n) + "$ steps)")
# pylab.plot(x, y)
# pylab.savefig("rand_walk"+str(n)+".png",bbox_inches="tight",dpi=600)
# pylab.show()
