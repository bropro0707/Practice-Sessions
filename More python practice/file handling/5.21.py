import csv
with open("compresult.csv","r")as file:
    reader = csv.reader(file)
    for i in reader:
        print(i)