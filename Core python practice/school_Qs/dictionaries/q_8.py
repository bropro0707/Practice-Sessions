d = {}
n = int(input("enter the Number of students: "))
for i in range(0,n):
    r,m = eval(input("Enter Roll no., Marks: "))
    d[r] =  m
print(d)
choice = str(input("Do you want to add more students(y/n): "))
while choice == "y":
    r,m = eval(input("Enter Roll no., Marks: "))
    d[r] =  m
    print(d)
    choice = str(input("Do you want to add more students(y/n): "))
else:
    print("thanks for using my program")