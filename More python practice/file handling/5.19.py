import csv
with open("csvfile.csv","w") as cfile:
    csvwrite = csv.writer(cfile)
    csvwrite.writerow(["Rollno.","Name","Marks"])
    for i in range(2):
        r = int(input("Ente the roll no.: "))
        n = str(input('Enter the name of the student: '))
        m = float(input("Enter the Marks of the student: "))
        strec = [r,n,m]
        csvwrite.writerow(strec)
