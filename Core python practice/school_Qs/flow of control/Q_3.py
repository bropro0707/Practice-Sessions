#SUM OF REPEATED NUMBER AND NON REPEATED
a = c = b = 0
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))
sum1 = a + b + c
print("The sum of three numbers are", sum1)
if a == b:
    sum2 = c
    print("The sum of non repeated numbers are", sum2)
elif a == c:
    sum2 =  b
    print("The sum of non repeated numbers are", sum2)
elif b == c:
    sum2 = a
    print("The sum of non repeated numbers are", sum2)
else:
    print("No repeated number inserted.")

print(":)")
