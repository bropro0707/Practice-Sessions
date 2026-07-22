# FIND IF THE INPUT IS PRIME OR NOT 
n = int(input("enter a number to find if it is prime or not: "))
a = int(n/2) + 1
for i in range ( 2,a ):
    if(n % i == 0):
        print(f"{n} is not a prime number")
        break
else:
    print(f"{n} is a prime number")
    