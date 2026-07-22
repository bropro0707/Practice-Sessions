b = str(input("Enter any name: "))
lenght =  len(b)
a = -lenght-1
n = 0
for i in range(-1,(-lenght-1), -1):
    a += i 
for i in range(0, lenght):
    n += i
print(b[a],"\t", b[n])