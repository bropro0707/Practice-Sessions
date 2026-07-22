#FIND WHICH NUMBER IS THE LARGEST
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))
if ( a>b and a>c ):
    print(f"{a} is the largest number")
if ( b>a and b>c):
    print(f"{b} is the largest number")
if ( c>a and c>b):
    print(f"{c} is the largest number")
print("Thanks")