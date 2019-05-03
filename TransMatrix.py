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

def transmat_moderate(dims):
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
