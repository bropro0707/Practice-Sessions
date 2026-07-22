el = [10, 23, "pitega"]
a = eval(input("enter the value to list: "))
if type(a) == type([]):
    el.extend(a)
elif type(a) == int:
    el.append(a)
print(el)