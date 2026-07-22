#FIND THE FACTORS OF INPUT 6 NUMBERS
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))
d = float(input("Enter 4th number: "))
e = float(input("Enter 5th number: "))
n = float(input("Divisor number: "))
count = 0
if a % n == 0:
    print(a)
    count += 1
if b % n == 0:
    print(b)
    count += 1
if c % n == 0:
    print(c)
    count += 1
if d % n == 0:
    print(d)
    count += 1
if e % n == 0:
    print(e)
    count += 1
print(f"{count} multipules of {n} are found")