# FIND SUM OF ONLY ODD NUMBER TILL THE INPUT
n = int(input("Enter the number: "))
a = 0
i = 1
while i <= n:
    a += i
    i += 2
print(a)