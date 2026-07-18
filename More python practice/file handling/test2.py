def primeno(m,n):
    pno = 0
    for i in range(m+1,n):
        if (i%2 == 0):
            pno +=1
    return pno
a = int(input("Enter the no."))
b = int(input("Enter the second no."))
print(primeno(a,b))