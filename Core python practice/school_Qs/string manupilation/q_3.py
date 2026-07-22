# a = int(input("Enter the number: "))
# b = str(a)
# len = len(b)
# for i in range(0,len):
#     if (b[i] =="0"):
#         print("Yes, it contains 0")
#     else:
#         print("No it not contains 0")

a = int(input("Enter the number: "))
b = str(a)
if "0" in b:
    print("Yes it contain 0")
else:
    print("No it not contain 0")