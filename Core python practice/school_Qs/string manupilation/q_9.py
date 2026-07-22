a = "bkl tu chutiya hain bhyadu"
len = len(a)
b = "u"
occurence = 0
for i in range(0,len):
    if a in b:
        occurence += 1
print(occurence)