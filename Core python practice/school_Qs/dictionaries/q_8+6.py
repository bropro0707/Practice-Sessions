d = {}
n = int(input("enter the Number of students: "))
for i in range(0,n):
    r,m = eval(input("Enter Roll no., Marks: "))
    d[r] =  m
print(d)
while True:
    choice = int(input('''1.for adding new student
    2.for updating student's number
    3.for quit: '''))

    if choice == 1:
        r,m = eval(input("Enter Roll no., Marks: "))
        d[r] =  m
        print(d)

    elif choice == 2:
        r = int(input("Enter the Rollno.: "))
        if r in d:
            d[r] = float(input("Enter the marks: "))
            print(d)
        else:
            print(f"There no such {r} Rollno.")

    elif choice == 3:
        print("thanks for using my program")
        break
    
    else:
        print("Invalid option :( ")