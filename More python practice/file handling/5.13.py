import pickle as pk
with open("myfile.dat","wb")as myfile:
    a = """My name is tabish. Working here"""
    pk.dump(a,myfile)
with open("myfile.dat","rb")as file:
    a = pk.load(file)
    print(a)