#FIND WHICH IS THE GREATEST INTEGERS OF ALL INPUTS 
# a = float(input("Enter 1st number: "))
# b = float(input("Enter 2nd number: "))
# c = float(input("Enter 3rd number: "))

# num = [a,b,c]

# num.sort(reverse=True)

# print(f"{num[0]} > {num[1]} > {num[2]}")


# or #

a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))

if a > b and a > c :
    if b > c:
        print(f"{a} > {b} > {c} ")
    else:
        print(f"{a} > {c} > {b}")
elif b > a and b > c:
    if a > c :
        print(f"{b} > {a} > {c} ")
    else:
        print(f"{b} > {c} > {a} ")
elif c > a and c > b:
    if a > b:
        print(f"{c} > {a} > {b} ")
    else:
        print(f"{c} > {b} > {a} ")
else:
    print("something went wrong")
