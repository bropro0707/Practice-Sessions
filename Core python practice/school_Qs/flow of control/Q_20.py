print("Enter the angle of the shape 'only 3 times' ")
angle1 = int(input("Enter the angle of shape: "))
angle2 = int(input("Enter the angle of shape: "))
angle3 = int(input("Enter the angle of shape: "))
if (angle1 + angle2 + angle3 == 180):
    if angle1 == 90:
        print("Triangle is right angle triangle")
    elif angle2 == 90:
        print("Triangle is right angle triangle")
    elif angle3 == 90:
        print("Triangle is right angle triangle")
    else:
        print("just a normal triangle yoo")
else:
    print("pata nahi magar triangle to nahi hain")