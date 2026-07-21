def determinant(x):
    a,b,c,d = x[0][0],x[0][1],x[1][0],x[1][1]
    return a*d - c*b
m = [[1,2],[3,4]]
print(determinant(m))
