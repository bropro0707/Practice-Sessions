import pickle as pk
# with open("stu.dat","ab")as sfile:
#     while True:
#         n = str(input("Enter the students name: ")) 
#         rollno = int(input("Enter the roll number: "))
#         data= [n,rollno]
#         pk.dump(data,sfile)
#         choice = input("Do you want to add more data(y/n): ")
#         if choice in "nN":
#             break 
with open("stu.dat","rb")as file: 
    a= pk.load(file)
    for i in a:
            
        if i[0] == "14":
            print("data of 14 roll no. present")
        elif i[0] !="14": 
            print("data of 14 roll no. not present")
        elif i[0] !="15": 
            print("data of 14 roll no. not present")
        if i[0] == "15":
            print("data of 15 roll no. present") 
            