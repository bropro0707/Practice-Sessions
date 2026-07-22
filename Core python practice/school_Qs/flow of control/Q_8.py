# FIND ARTHMETIC RESULT OF GIVEN TWO NUMBER
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
opertor = str(input('''for addition (+)
for mutlipication (*)
for subtration (-)
for division (/) : '''))
if opertor == "+":
    print(a + b)
elif opertor == "-":
    print(a - b)
elif opertor == "*":
    print ( a*b)
else:
    print ( a / b)
print("Thanks")