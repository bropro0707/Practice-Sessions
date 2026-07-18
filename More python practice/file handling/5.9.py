import pickle as pk
with open("sdata.dat","ab")as sfile:
    while True:
        srec = {}
        sname = str(input("Enter the name of the student: "))
        rollno = int(input("Enter the Roll number: "))
        marks = int(input("write the average marks obtain: "))
        choice = input("do you want to add more student rec (y/n): ").strip().lower()
        srec["Name"] = sname
        srec["Rollno."] = rollno
        srec["marks"] = marks
        pk.dump(srec,sfile)
        if choice in "Nn":
            break