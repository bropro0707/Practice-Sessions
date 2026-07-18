import csv
print("-----------WELCOME TO THE CAFE MANEGMENT PROGRAM-----------")
print("PLEASE ENTER YOUR OCCUPATION")
c = int(input("""1.STAFF
2.CUSTOMER: """))
if c == 1:
    p = input("Enter password: ")
    if p == "abc123":
        print("===============================================================")
        print("---------------------- BARVI PASS CAFE ------------------------")
        print("===============================================================")

        print("FOUNDER/CEO :- MR MOHAMMED TABISH KHAN")
        print("CEOO :- MR SAURAV YADAV")


        def add_employee():
            with open("empdata.csv","a",newline="") as empf:
                emp_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                empdata = [emp_id, name, position]
                w = csv.writer(empf,delimiter="|")
                w.writerow(empdata)
                print("✅ Employee added successfully.")

        def mark_attendance():
            emp_id = input("Enter Employee ID: ")
            with open("empdata.csv","r")as empf:
                r = csv.reader(empf, delimiter="|")
                for emp in r:
                        if emp[0] == emp_id:
                            with open("empattendence.csv","a")as aemp:
                                w = csv.writer(aemp,delimiter="|")
                                attendance = [emp[1],"PRESENT"]
                                w.writerow(attendance)
                                print("✅Attendance marked for", emp[1])
                                return
                else:
                    print("\n")
                    print("Employee not found.")

        def sale():
            with open("Billdata.csv","r")as sales:
                    total = 0
                    nitems = 0
                    r = csv.reader(sales,delimiter="|")
                    print("\n")
                    print("ITMES: ")
                    for t in r:
                        a = float(t[1])
                        total += a
                        nitems += 1
                        print(f"{t[0]}," ,end="")
                    print()
                    print("--------------------------------------")
                    print("TOTAL NUMBER OF ITMES: ",nitems)
                    print("--------------------------------------")
                    print(f"TOTAL : ₹{total}")
                    print("--------------------------------------")
                                    
        def show_employees():
            with open("empdata.csv","r")as datfemp:
                r = csv.reader(datfemp,delimiter="|")
                print("\n----------- Employee List -------------")
                for emp in r:
                    if emp[0] == " ":
                        print("No employees found.")
                        return
                    else:
                            
                        print("ID:", emp[0], ", Name:", emp[1], ", Position:", emp[2],)

        def complain(x):
            name = str(input("Enter your name: "))
            with open("complain.txt","a") as cfile:
                cfile.write("\n")
                cfile.write(f"Complain from: {name}")
                cfile.write("\n")
                cfile.write("------------------------------------------------")
                cfile.write("\n")
                cfile.write(x)
                cfile.write("\n")
                cfile.write("------------------------------------------------")
                cfile.write("\n")


            

        while True:
            print("\n--- Cafe Management Menu ---")
            print("1. Add Employee")
            print("2. Mark Attendance")
            print("3. Show Sales")
            print("4. Show Employees")
            print("5. Any Complain")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                add_employee()
            elif choice == "2":
                mark_attendance()
            elif choice == "3":
                sale()
            elif choice == "4":
                show_employees()
            elif choice == "5":
                comp = str(input("Enter your complain: "))
                complain(comp)

            
                print("Goodbye! FIR MILENGE.")
            
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("if you don't have password please contact the manager")

if c == 2:


    menu = [
    ["Americano",200],
    ["Latte",200],
    ["Yadav Ji Special",250],
    ["Mocha",350],
    ["Soft Drink",30],
    ["Abduls Briyani",550],
    ["Farm Pizza",250],
    ["Cheese Pasta",250],
    ["Manchurian",60],
    ["Coffee",20],
    ["Shawarma",200]
    ]
    def display():
        print("================ BARVI PASS CAFE ================")
        print("Sno.  |Items             |Price(Not Including GST)")
        print("-----------------------------------------------")
        for i in range(len(menu)):
            print(f"{i:5} | {menu[i][0]:16} | {menu[i][1]}")
        print("-----------------------------------------------")
        
    def order():
        global order
        order = []
        print("\n")
        print('Write "done" if you do not want to add more items')
        while True:
            citem = input("Enter the serial no. of your dish: ")
            
            if citem.isdigit():
                order.append(int(citem))
                print("--Order Taken--")

            elif citem in "doneDONE":
                break


    def bill():
        k = []
        print("\n")
        print("BILL")
        print("-------------------------------------------------")
        print("Items: ",  end="")

        for j in order:
                print(menu[j][0], end=", ")
                k.append(menu[j][1])
        s = sum(k) 
        print(f"\nTOTAL AMOUNT: ₹{s}")
        print("-------------------------------------------------")

    def store():
        with open("billdata.csv","a+",newline="")as file:
            w = csv.writer(file,delimiter="|")
            for i in order:    
                w.writerow([menu[i][0],menu[i][1]])

    display()
    order()
    bill()
    store()

else:
    print("please run the programe again")