# FIND THE ADDITION OF THE NUMBER MULTIPLE TIMES
count = answer = 0
ans = "y"
while ans == "y":
    n = int(input("enter the number:" ))
    if n < 0:
        print( " the value is  smaller than 0 not valid")
        break
    answer += n
    ans = input("want to enter more number (y/n)")
    count += 1
else: 
    print(f"you entered {count} number so far ")
print(f"the sum of entered number is {answer}")