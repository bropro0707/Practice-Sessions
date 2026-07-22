roll = []
marks =[]
for i in range(0,4):
    r, m = eval(input("Enter roll no., marks: "))
    roll.append(r)
    marks.append(m)
if marks[1] > 75:
    print("roll no.2 has scored over 75")
else:
    pass
d = {roll[0]:marks[0],roll[1]:marks[1],roll[2]:marks[2],
     roll[3]:marks[3]}
print(d)