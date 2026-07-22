Marks = {1:45,2:65,3:89,4:59,5:52.25}
print(Marks)
choice = int(input("Enter the Rollno. you want to delete: "))
if choice in Marks:
    del Marks[choice]
    print(Marks)
else:
    print("Can't find the Rollno.")