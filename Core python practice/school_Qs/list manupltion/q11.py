n = [2,2,2,77,000,98,98,98,12,12,12,12,12,12]
e = int(input("Enter the element to find its frequency: "))
count = 0
for i in n:
    if i == e:
        count += 1
if count == 0:
    print("can't the value")
else:
    print(f"found {e} '{count}' times")
