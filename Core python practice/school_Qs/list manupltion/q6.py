a = [1, 23,24,23]
print(a)
print("""(1.insert)
(2.delete)
(3.exit)""")
choice = int(input("Enter the your choice: "))
if choice == 1:
    insert = eval(input("Enter the what you want: "))
    if type(insert) == type([]):
        a.extend(insert)
        print(a)
    else:
        a.append(insert)
        print(a)
elif choice == 2:
    choice1 = int(input("""(1.by position)
(2.by value)
Enter your choice: """))
    if choice1 == 1:
        d1 = int(input("enter the position of value: "))
        a.remove(a[d1])
        print(a)
    elif choice == 2:
        d2 = int(input("Enter the value: "))
        for i in a:
            if i == d2:
                a.remove(d2)
                print(a)
            else:
                print("can't find the item")
else:
    print("bye")