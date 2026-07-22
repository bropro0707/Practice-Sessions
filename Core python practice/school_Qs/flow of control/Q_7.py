#FIND PERIMETER OR AREA OF THE CIRCLE
choice = int(input('''To find perimeter of circle (1)
To find area of circle (2)
Enter your choice: '''))
if choice == 1:
    radius = float(input("Enter the radius of the circle: "))
    print( f"The perimeter of the circle of radius {radius} is", 2*3.14*radius)

else:
    radius = int(input("Enter the radius of the circle: "))
    print(f"the area of the circle of radius {radius} is", 3.14*radius*radius)