d = {}
n = int(input("enter the Number of students: "))
for i in range(0,n):
    r,m = eval(input("Enter Roll no., Marks: "))
    d[r] =  m
print(d)
choice = "y"
while choice == "y":
    choice = str(input("For changing the marks of a rollno.(y/n): "))
    r = int(input("Enter the Rollno.: "))
    if r in d:
        d[r] = float(input("Enter the marks: "))
        print(d)
    else:
        print(f"There no such {r} Rollno.")
else:
    print("thanks for using my program")