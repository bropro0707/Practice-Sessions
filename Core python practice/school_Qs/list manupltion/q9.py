a = eval(input("Enter the list to find its mean: "))
l = len(a)
i= sum = 0
for i in a:
    sum += i
mean = sum/l
print(mean)