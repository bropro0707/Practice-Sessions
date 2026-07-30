# 2by2 matrix multiplication
def mat_mul_2(A,B):
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0],A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]
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

#test
a = [[1,2,3],[3,4,5],[5,6,7]] 
b = [[8,9,0],[2,4,4],[5,9,9]]

print(mat_mul_3(a,b))