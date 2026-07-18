import pickle as pk
with open("emp.dat","wb")as file :
    emp1 = {'empname':'Tabish','salary':'800000','age':35}
    emp2 = {'empname':'bropro','salary':'8000','age':24}
    emp3 = {'empname':'krolro','salary':'8000000','age':40}
    emp4 = {'empname':'grojro','salary':'8','age':5}
    emprec = emp1,emp2,emp3,emp4
    pk.dump(emprec,file)