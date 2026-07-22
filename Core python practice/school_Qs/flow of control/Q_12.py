# FIND THE SUM OF N NATURAL NUMBERS
n = int(input("Enter the number to find the sum of natural number till the input: "))
for i in range(1,n):
    n += i
print(n)