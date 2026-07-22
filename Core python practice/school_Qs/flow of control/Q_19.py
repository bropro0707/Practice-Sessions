#SLICING OF THE GIVEN NUMBERS
n = int(input("Enter a 6 digit number: "))
n = str(n)
if len(n) == 6:
    print(n[0:2])
    print(n[2:4])
    print(n[4:7])
else:
    print ("enter only 6 digit number plz")