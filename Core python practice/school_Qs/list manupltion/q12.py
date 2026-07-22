a = eval(input("Enter the ele in as list 1 to 12: "))
l = len(a)
for i in range(0,l):
    if a[i] > 10:
        a.remove(a[i])
        a.insert(a[i-1],10)
print(a)