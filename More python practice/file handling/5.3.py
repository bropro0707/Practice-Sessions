while True:
    choice = str(input("Do you want to enter data of new student(y/n): "))
    if choice in "nN":
        break
    else:
        with open("Marks.txt", "a") as fMarks:
            rn= int(input("Enter the roll no. of the student: "))
            name = input("Enter student's name: ")
            marks = float(input("Enter the over all marks obtained: "))
            rec = f"{name},{str(rn)},{str(marks)}"
            if fMarks.tell() != 0:
                rec = "\n" + rec
            fMarks.write(rec)