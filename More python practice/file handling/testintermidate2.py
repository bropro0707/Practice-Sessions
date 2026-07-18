import csv
with open("marks.csv","r")as f:
    students = []
    t_no=0
    r= csv.DictReader(f)
    for i in r:
        marks = int(i["Marks"])
        student = {
            "Rollno.":i["Rollno."],
            "Name":i["Name"],
            "Marks":i["Marks"]
        }
        students.append(student)
    t_no += marks

average = t_no/4

output = []
for i in students:
    o_r = {
        "Name":i["Name"],
        "Rollno.":i["Rollno."],
        "Marks":i["Marks"],
        "average":average
    }
    output.append(o_r)

with open("resul.csv","w")as file:
    structure = ["Name","Rollno.","Marks","average"]
    dw = csv.DictWriter(file,fieldnames=structure)
    dw.writeheader()
    dw.writerows(output)
    
