import pickle as pk
with open("myfile.dat","rb")as file:
    a = pk.load(file)
    lst = a.split("o")
    print(lst[0])