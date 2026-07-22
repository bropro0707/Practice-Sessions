rent_flat = {"Ashoka garden":{"area":"2BHK","Monthly":10000},
"Govindpura":{"area":"3BHK", "Monthly":9000},
"M.P nagar":{"area":"1BHK", "Monthly": 20000}}
rent_duplex = {"Ashoka garden":{"area":"5BHK","Monthly":15000},
"Kolar":{"area":"4BHK", "Monthly":10000}}
rent_singlex = {"Ashok Vihaar":{"area":"2BHK","Monthly":5000},
"Itvara":{"area":"3BHK", "Monthly":9000},
"Budhvara":{"area":"1BHK", "Monthly": 1000}}
rent_farmh = {}

buy_flat = {"Ayodhya Bypass":{"area":"3BHK","Prize":4000000},
"Amaltash":{"area":"4BHK", "Prize":5000000},
"Kohefiza":{"area":"4BHK","Prize":20000000}}
buy_duplex = {"Ashoka garden":{"area":"3BHK","Prize":8000000},
"Kohefiza":{"area":"7BHK","Prize":50000000},
"M.P nagar":{"area":"2BHK","Prize":30000000}}
buy_singlex = {"Govindpura":{"area":"3BHK", "Prize":3000000},
"Sunder nagar":{"area":"2BHK","Prize":3000000}}
buy_farmh = {"Ethkhedi":{"area":"2BHK","Prize":800000}}
buy_penthouse = {}

#Choice for Property
print("-------------PROPERTY MANAGMENT------------")
c = int(input('''1.Property for rent
2.Property for buying
3.Providing property for rent/selling : '''))

#Choice for rent
if c == 1:
    print("-----------Property for RENT------------")
    c_rent = int(input('''  1.For Flat
    2. For Duplex
    3. for singlex
    4. Farm house: '''))

    if c_rent == 1:
        for key in rent_flat:
            print("----------------Flat for rent------------------")
            print(key)
            print("Area:", str(rent_flat[key]["area"]))
            print("Monthly rent:", str(rent_flat[key]["Monthly"]))
        print("\n")
        choice = str(input("Enter the name of the area you want property(with capital letter): "))
        if choice in rent_flat:
            print(f"As we got to know you want propety in {choice}")
            print("Now our agent will call you for further information")
            print("Thankyou for choosing us :)")
        else:
            print("invalid input :(")
            print("Please take care of capital letters")

    elif c_rent == 2:
        for key in rent_duplex:
            print("----------------dupelx for rent------------------")
            print(key)
            print("Area:", str(rent_duplex[key]["area"]))
            print("Monthly rent:", str(rent_duplex[key]["Monthly"]))
        print("\n")
        choice = str(input("Enter the name of the area you want property(with capital letter): "))
        if choice in rent_duplex:
                print(f"As we got to know you want propety in {choice}")
                print("Now our agent will call you for further information")
                print("Thankyou for choosing us :)")
        else:
                print("invalid input :(")
                print("Please take care of capital letters")
    
    elif c_rent == 3:
            for key in rent_singlex:
                print("----------------Singlex for rent------------------")
                print(key)
                print("Area:", str(rent_singlex[key]["area"]))
                print("Monthly rent:", str(rent_singlex[key]["Monthly"]))
            print("\n")
            choice = str(input("Enter the name of the area you want property(with capital letter): "))
            if choice in rent_singlex:
                print(f"As we got to know you want propety in {choice}")
                print("Now our agent will call you for further information")
                print("Thankyou for choosing us :)")
            else:
                print("invalid input :(")
                print("Please take care of capital letters")
        
    
    elif c_rent == 4:
        print("We don't have Farm houses for rent")
        print("Sorry for inconvenience")
    
    else:
        print("Invalid Input")

#Choice for buying
elif c == 2:
    print("-----------Property for BUYING------------")
    c_buy = int(input('''1.For Flat
    2. For Duplex
    3. For singlex
    4. For farm house
    5. For Penthouse: '''))
    if c_buy == 1:
        for key in buy_flat:
            print("----------------flat for buying------------------")
            print(key)
            print("Area:", str(buy_flat[key]["area"]))
            print("Prize:", str(buy_flat[key]["Prize"]))
        print("\n")
        choice = str(input("Enter the name of the area you want property(with capital letter): "))
        if choice in buy_flat:
                print(f"As we got to know you want propety in {choice}")
                print("Now our agent will call you for further information")
                print("Thankyou for choosing us :)")
        else:
                print("invalid input :(")
                print("Please take care of capital letters")        
    elif c_buy == 2:
        for key in buy_duplex:
            print("--------------duplex for buying----------------")
            print(key)
            print("Area:", str(buy_duplex [key]["area"]))
            print("Prize:", str(buy_duplex [key]["Prize"]))
        print("\n")
        choice = str(input("Enter the name of the area you want property(with capital letter): "))
        if choice in buy_duplex :
                print(f"As we got to know you want propety in {choice}")
                print("Now our agent will call you for further information")
                print("Thankyou for choosing us :)")
        else:
                print("invalid input :(")
                print("Please take care of capital letters")     
    elif c_buy == 3:
        for key in buy_singlex:
            print("--------------singlex for buying----------------")
            print(key)
            print("Area:", str(buy_singlex [key]["area"]))
            print("Prize:", str(buy_singlex [key]["Prize"]))
        print("\n")
        choice = str(input("Enter the name of the area you want property(with capital letter): "))
        if choice in buy_singlex :
                print(f"As we got to know you want propety in {choice}")
                print("Now our agent will call you for further information")
                print("Thankyou for choosing us :)")
        else:
                print("invalid input :(")
                print("Please take care of capital letters")     
    elif c_buy == 4:
        for key in buy_farmh:
            print("--------------farm house for buying----------------")
            print(key)
            print("Area:", str(buy_farmh [key]["area"]))
            print("Prize:", str(buy_farmh [key]["Prize"]))
        print("\n")
        choice = str(input("Enter the name of the area you want property(with capital letter): "))
        if choice in buy_farmh :
                print(f"As we got to know you want propety in {choice}")
                print("Now our agent will call you for further information")
                print("Thankyou for choosing us :)")
        else:
                print("invalid input :(")
                print("Please take care of capital letters")
    elif c_buy == 5:
         print("Sorry we don't have any penthouse available currently")
         print("Sorry for inconvenience :(")
    else:
        print("Invalid Input")

#choice for providing
elif c == 3:
    print("---------------Providing Property---------------")
    choice = int(input('''1.For rent
2.for selling: '''))
    if choice == 1:
        print("-------------Rent your Property-----------------")
        choice_rent = int(input('''1.For Flat
2. For Duplex
3. for singlex
4. Farm house: '''))
        a = str(input("Enter the name of the area: "))
        s = str(input("Enter the area of the property: "))
        p = int(input("Enter the prize of per month: "))
        if choice_rent == 1:
            rent_flat[a] = {"area":s,"Prize":p}
            print("\n")
            print("Your details of the property has succesfully uploaded to our server")
            print("Our team will contact you for further verification")
            print("THANK YOU FOR CHOOSING US")
        elif choice_rent == 2:
            rent_duplex[a] = {"area":s,"Prize":p}
            print("\n")
            print("Your details of the property has succesfully uploaded to our server")
            print("Our team will contact you for further verification")
            print("THANK YOU FOR CHOOSING US")
        elif choice_rent == 3:
            rent_singlex[a] = {"area":s,"Prize":p}
            print("\n")
            print("Your details of the property has succesfully uploaded to our server")
            print("Our team will contact you for further verification")
            print("THANK YOU FOR CHOOSING US")
        elif choice_rent == 4:
            rent_farmh[a] = {"area":s,"Prize":p}
            print("\n")
            print("Your details of the property has succesfully uploaded to our server")
            print("Our team will contact you for further verification")
            print("THANK YOU FOR CHOOSING US")
        else:
            print("Invalid input")

    elif choice == 2:
        print("-------------Sell your Property-----------------")
        choice_buy = int(input('''1.Flat
2. Duplex
3. Singlex
4. Farm house
5. Penthouse: '''))
        a = str(input("Enter the name of the area: "))
        s = str(input("Enter the area of the property: "))
        p = int(input("Enter the prize: "))
        if choice_buy == 1:
            buy_flat[a] = {"area":s,"Prize":p}
            print("\n")
            print("Your details of the property has succesfully uploaded to our server")
            print("Our team will contact you for further verification")
            print("THANK YOU FOR CHOOSING US")
        elif choice_buy == 2:
            buy_duplex[a] = {"area":s,"Prize":p}
            print("\n")
            print("Your details of the property has succesfully uploaded to our server")
            print("Our team will contact you for further verification")
            print("THANK YOU FOR CHOOSING US")
        elif choice_buy == 3:
            buy_singlex[a] = {"area":s,"Prize":p}
            print("\n")
            print("Your details of the property has succesfully uploaded to our server")
            print("Our team will contact you for further verification")
            print("THANK YOU FOR CHOOSING US")
        elif choice_buy == 4:
            buy_farmh[a] = {"area":s,"Prize":p}
            print("\n")
            print("Your details of the property has succesfully uploaded to our server")
            print("Our team will contact you for further verification")
            print("THANK YOU FOR CHOOSING US")
        elif choice_buy == 5:
            buy_penthouse[a] = {"area":s,"Prize":p}
            print("\n")
            print("Your details of the property has succesfully uploaded to our server")
            print("Our team will contact you for further verification")
            print("THANK YOU FOR CHOOSING US")
        else:
            print("Invalid input")
    else:
        print("Invalid Input")


else:
    print("invalid input")