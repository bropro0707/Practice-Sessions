import math

# streching the vector
def scaling(x,y):
    return [[x,0],[y,0]]

#Rotating matrix counter clock vise
def rotating(theta):
    c = math.cos(theta)
    s = math.sin(theta)
    return [[c,-s],[s,c]]


