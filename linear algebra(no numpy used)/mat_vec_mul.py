def dot(a,b):
    return sum(x*y for x,y in zip(a,b))
def matvecmul(M,v):
    return [dot(row,v) for row in M]
m = [[1,2],[3,4]]
v=[1,2]
print(matvecmul(m,v))
