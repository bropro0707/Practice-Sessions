with open("text1.txt","r") as text:
    bytes = text.read()
    size = len(bytes)
    print("No. of bytes:",size)