a = input("Enter your username: ")
n = input("Enter your pcode (make sure its not a part of username): ")
b = str(a)
v = str(n)
if n in b:
    print("invalid please don't do repetition")
elif v == "Trident11":
    print("you are good to go to next stage")
else:
    print("invalid pcode")