a = input("Enter the string bro come on:")
lower = upper = alphabet = digits = symbol = 0
for i in a:
    if a.islower():
        lower += 1
    elif a.isupper():
        upper += 1
    elif a.isalpha():
        alphabet += 1
    elif a.isdigit():
        digits += 1
    elif a.isalnum():
        symbol += 1
print("Number of uppercase letter: ",upper)
print("Number of alphabet: ",alphabet)
print("Number of symbols: ",symbol)
print("Number of lowercase letter: ",lower)
print("Number of digits: ",digits)
