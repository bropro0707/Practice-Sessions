with open("story.txt","r")as f:
    lines = f.readlines()
    Tlines = len(lines)
    Twords = 0
    Tchar = 0
    for l in lines:
        words = l.split()
        Twords += len(words)
        Tchar += len(l)
    
    print(Tlines)
    print(Twords)
    print(Tchar)

