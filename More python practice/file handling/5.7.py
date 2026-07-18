with open("text1.txt", "r")as file:
    text = file.read()
    vowels = 0
    consonants = 0
    for i in text:
        if i.isalpha():
            if i in "aeiouAEIOU":
                vowels += 1
            else:
                consonants += 1
        else:
            pass
print("The no. of vowel:",vowels)
print("The no. of consonents:",consonants)
print("text1.txt")