with open("text2.txt", "r") as text:
    for line in text:          
        modified_line = line.replace(" ", "#")  
        print(modified_line, end="")  