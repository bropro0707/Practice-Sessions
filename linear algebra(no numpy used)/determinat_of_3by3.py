def mini_deter(x):
    return x[0][0]*x[1][1] - x[0][1]*x[1][0]

def determinant(x):
    total = 0
    total += x[0][0] * mini_deter([[x[1][1], x[1][2]],
                                   [x[2][1], x[2][2]]])
    total -= x[0][1] * mini_deter([[x[1][0], x[1][2]],
                                   [x[2][0], x[2][2]]])
    total += x[0][2] * mini_deter([[x[1][0], x[1][1]],
                                   [x[2][0], x[2][1]]])
    return total
