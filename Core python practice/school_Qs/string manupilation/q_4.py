a = input("Enter your username: ")
n = input("Enter your code (make sure its not a part of username): ")
b = str(a)
v = str(n)
if n in a:
    print("invalid please don't do repetition")
else:
    print("you are good to go to next stage")