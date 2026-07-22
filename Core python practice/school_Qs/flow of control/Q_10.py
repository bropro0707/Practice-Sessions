#FIND THE SOLUTION OF THE QUADRATIC EQUATION 
import math

print("for find the solution of the 'ax**2+bx+c', enter the cofficient given below")
a = int(input("Enter the value of cofficient a: "))
b = int(input("Enter the value of cofficient b: "))
c = int(input("Enter the value of cofficient c: "))

if a == 0:
    print ( "Value of a must not be zero")
else:
    D = b*b-4*a*c
    if D == 0:
        ans = -b / (2*a)
        print(ans)
    elif D > 0:
        ans1 = (-b + math.sqrt(D))/(2*a)
        ans2 = (-b - math.sqrt(D))/(2*a)
        print (f"roots are {ans1} and {ans2}")
    else:
        print ("Roots are imaginary")

# BODMAS bhi lagata hain bhai (dimag kharab)