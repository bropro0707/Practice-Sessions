import csv 
with open("compresult.csv","w")as cfile:
    csvwrite = csv.writer(cfile)
    csvwrite.writerow(["Name","Points","Ranks"])
    for i in range(5):
        n = str(input("Enter the name of the student: "))
        p = (input("Enter the points obtain of the student: "))
        r = (input("Enter the rank of the student: "))
        csvwrite.writerow([n,p,r])