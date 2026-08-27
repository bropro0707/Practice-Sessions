import math
# ------------ basic ops -------------
# 3by3 matrix multiplication
def mat_mul_3(x,y):
    if not x or not y or not x[0]:
        raise ValueError("Enter proper matrices")
    if len(x[0]) != len(y):
        raise ValueError("Invalid dimensions of Matrices for multiplication")
    result = [[0] * len(y[0]) for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(y[0])):
            total = 0
            for k in range(len(x[0])):
                total += x[i][k]*y[k][j]
            result[i][j] = total
    return result

# 2by2 matrix multiplication
def mat_mul_2(A,B):
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0],A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]

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

#------------------- Transformation ----------------

#additon of 2 vectors
def vecadd(x,y):
    return [sum(x) for x in zip(x,y)]

# streching the vector
def scaling(x,y):
    return [[x,0],[0,y] ]

#Rotating matrix
def rotating_counter_clock(theta):
    c = math.cos(theta)
    s = math.sin(theta)
    return [[c,-s],[s,c]]


def rotating_clock(theta):
    c = math.cos(theta)
    s = math.sin(theta)
    return [[c,s],[-s,c]]

#Shearing
def shear_horizontal(x):
    return [[1,x],[0,1]]

def shear_vertical(x):
    return [[1,0],[x,1]]

#scalling vectors by a cofficient
def linear_combo(vectors, coffi):

    scaling= []

    for i in range(len(vectors)):
        row = []
        for j in range(len(vectors)):
            if i == j:
                row.append(coffi)
            else:
                row.append(0)
        scaling.append(row)

    if len(vectors) == 2:
         return mat_mul_2(vectors,scaling)
    elif len(vectors) == 3:
        return mat_mul_3(vectors,scaling)
        

#--------------------------- test ---------------------------
v = [[3,-2,0],[8,5,0],[7,9,1]]
result = linear_combo(v,2)
print(result)
