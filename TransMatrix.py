import numpy as np

def transmat1(dim1,dim2):
    dim = dim1 * dim2

    #Build matrix with zeros
    matrix = np.zeros([dim+2, dim+2])

    #populate transition matrix
    for i in range(dim+2):
        for j in range(dim+2):
            if math.abs(i-j)
                matrix[i][j] = 



    return matrix



# transition model:
    # generates a 16x16 matrix describing probability of moving from any square
    # to any other
    def compute_transition_model(self):

        # empty transition matrix
        trans_matrix = np.zeros((16, 16))

        # loop through the maze
        for y, column in enumerate(self.start_state):
            for x, value in enumerate(column):

                # convert to what value would be in a 1x16 array
                current = self.one_dimize((x, y))

                # get neighbors and track the total possible moves from square
                moves = self.get_moves((x, y))
                total_moves = len(moves)

                # for each move, incrememnt the probability in the matrix by
                # 1/total (probability of making that move from that square)
                for move in moves:
                    next = self.one_dimize(move)
                    trans_matrix[next, current] += 1/total_moves

        # transpose for multiplication
        return np.transpose(trans_matrix)

    # returns a list of legal moves from a given square (tuple)
