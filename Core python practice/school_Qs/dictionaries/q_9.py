Employes = {"tabish":{"salary":120000,"area":"Data science"},
            "munna mobile":{"salary":100000,"area":"Game development"}}
for key in Employes:
    print("---------- Details of Employes -----------")
    print("Employe",key,";")
    print("salary", str(Employes[key]["salary"])) 
    print("AREA", (Employes[key]["area"]))

