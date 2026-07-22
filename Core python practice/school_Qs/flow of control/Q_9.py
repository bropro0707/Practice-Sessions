#FIND THE TYPE OF THE GIVEN INPUT
n = input("Enter a single input: ")

if n >= "A" and n <= "Z":
        print("the input is uppercase string")
elif n >= "a" and n <= "z" :
    print("the input is a lowercase string ")
elif n >= "0" and n <= "9":
     print("The input is a digit")
else:
    print("the input is a special character")