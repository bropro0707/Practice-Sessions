# Determinant od 2×2 matrix
def determinant2by2(x):
    a,b,c,d = x[0][0],x[0][1],x[1][0],x[1][1]
    return a*d - c*b

# determinant od 3×3 matrix
def determinant3by3(x):
    total = 0
    total += x[0][0] * determinant2by2([[x[1][1], x[1][2]],
                                   [x[2][1], x[2][2]]])
    total -= x[0][1] * determinant2by2([[x[1][0], x[1][2]],
                                   [x[2][0], x[2][2]]])
    total += x[0][2] * determinant2by2([[x[1][0], x[1][1]],
                                   [x[2][0], x[2][1]]])
    return total

#dot product
def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

#matrix and vector mulitiplication (2d)
def matvecmul(M,v):
    return [dot(row,v) for row in M]

#Transpose
def transpose(x):
    return [list(coms) for coms in zip(*x)]
