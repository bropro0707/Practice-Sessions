a = [12,14,32,534]
choice = int(input("Enter the number you want to find: "))
l = len(a)
for i in range(0,l):
    if a[i] == choice:
        print("element has found at",i)
        break
else:
    print("element is not there")