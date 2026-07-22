# FIND THE FACTORIAL OF THE GIVEN NUMBER
n = int(input("Enter the number to find its factorial: "))
if n == 0:
    print("1")
else:
    for i in range (1,n):
        n *= i
    print(n)