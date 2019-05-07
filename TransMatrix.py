import numpy as np

#Equal probability of each sqare and itself
def transmat_simple(dims):
    dim_trans = dims**2  # transition matrix is n squared by n squared

    # build matrix with zeros
    matrix = np.zeros([dim_trans, dim_trans])

    #populate transition matrix
    for i in range(dim_trans):
        for j in range(dim_trans):
            if i == j:
                matrix[i][j] += 0.2
                matrix[i][min(dim_trans-1, j+1)] += 0.2
                matrix[i][max(0, j-1)] += 0.2
                matrix[i][min(j+dims, dim_trans-1)] += 0.2
                matrix[i][max(0, j-dims)] += 0.2

    return np.transpose(matrix)

#Equal probability for all 10 squares adjacent
def transmat_moderate(dims):
    dim_trans = dims**2  # transition matrix is n squared by n squared

    # build matrix with zeros
    matrix = np.zeros([dim_trans, dim_trans])

    #populate transition matrix
    for i in range(dim_trans):
        for j in range(dim_trans):
            if i == j:
                matrix[i][j] += 0.1
                matrix[i][min(dim_trans-1, j+1)] += 0.1
                matrix[i][max(0, j-1)] += 0.1
                matrix[i][min(j+dims, dim_trans-1)] += 0.1
                matrix[i][max(0, j-dims)] += 0.1

                matrix[i+1][min(dim_trans-1, j+1)] += 0.1
                matrix[i+1][max(0, j-1)] += 0.1
                matrix[i-1][min(j+dims, dim_trans-1)] += 0.1
                matrix[i-1][max(0, j-dims)] += 0.1

    return np.transpose(matrix)

#Normally distributed probabilities around central square two wide
def transmat_advanced1(dims):
    dim_trans = dims**2  # transition matrix is n squared by n squared

    # build matrix with zeros
    matrix = np.zeros([dim_trans, dim_trans])

    #populate transition matrix
    for i in range(dim_trans):
        for j in range(dim_trans):
            if i == j:
                matrix[i][j] += 0.2
                matrix[i][min(dim_trans-1, j+1)] += 0.2
                matrix[i][max(0, j-1)] += 0.2
                matrix[i][min(j+dims, dim_trans-1)] += 0.2
                matrix[i][max(0, j-dims)] += 0.2

    return np.transpose(matrix)

#Implement boundaries with farm?
def transmat_advanced2(dims):
    dim_trans = dims**2  # transition matrix is n squared by n squared

    # build matrix with zeros
    matrix = np.zeros([dim_trans, dim_trans])

    #populate transition matrix
    for i in range(dim_trans):
        for j in range(dim_trans):
            if i == j:
                matrix[i][j] += 0.2
                matrix[i][min(dim_trans-1, j+1)] += 0.2
                matrix[i][max(0, j-1)] += 0.2
                matrix[i][min(j+dims, dim_trans-1)] += 0.2
                matrix[i][max(0, j-dims)] += 0.2

    return np.transpose(matrix)


# x = transmat_simple(4)
# print(x)
# print(np.transpose(x))
