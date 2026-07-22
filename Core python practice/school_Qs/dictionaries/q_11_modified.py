Marks = {1:45,2:65,3:89,4:59,5:52.25}
print(Marks)
while True:
    choice = int(input('''1.To delete rollno.
2.Quit: '''))
    if choice == 1: 
        roll_to_delete = int(input("Enter the Rollno. you want to delete: "))
        if roll_to_delete in Marks:
            del Marks[roll_to_delete]
            print(Marks)
        else:
            print("Can't find the Rollno.")
    elif choice == 2:
        print("Thanks for using programe")
        break
    if not Marks: 
        print("The dictionary is now empty.")
        break
    else:
        print("invalid input")
