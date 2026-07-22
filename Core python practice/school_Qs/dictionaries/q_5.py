d = {}
n = int(input("enter the Number of students: "))
for i in range(0,n):
    r,m = eval(input("Enter Roll no., Marks: "))
    d[r] =  m
print(d)