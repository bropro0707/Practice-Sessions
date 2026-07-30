import math
# ------------ basic ops -------------
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


#--------------------------- test ---------------------------

a = scaling(1,1)
b = shear_horizontal(1)
comb = mat_mul_2(b,a)

v = [1,0]
result = matvecmul(comb,v)
print(result)
