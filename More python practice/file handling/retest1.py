with open("data.txt","r") as f:
    text = f.readlines()
    n=1
    for i in range(len(text)):
        print(n,":",text[i].strip())
        n+=1
