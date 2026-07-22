n = eval(input("Enter the number: "))
l = len(n)
mine = n[0]
mini = 0
for i in range(0,l):
    if n[i] < mine:
        mine = n[i]
        mini = i
print(mine)
print(mini)