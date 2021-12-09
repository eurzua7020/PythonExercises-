#9 Paint Calculator
#to round UP in python we'll use the MATH module and ceil() method
import math
gallon = 350 #per the instructions a gallon of paint covers 350 square feet
shapeRoom = int(input('Please enter the number corresponding to you ceiling shape\nEnter 1 for square or rectangle\nEnter 2 for Circle or round\nEnter 3 for L-Shaped'))
if (shapeRoom == 1):
    while True:
        try:
            ceilingL = float(input("what is the length of the ceiling in feet?"))
            break
        except ValueError:
            print("Please use numbers only")

    while True:
        try:
            ceilingW = float(input("what is the width of the ceiling? in feet"))
            break
        except ValueError:
            print("Please use numbers only")
    ceilingA = ceilingL * ceilingW
    gallons_needed = math.ceil(ceilingA /gallon)
    print(f'You will need to purchase {gallons_needed} gallons of')
    print(f'paint to cover {ceilingA} square feet.')
#for this part remember the area of a circle is A = Pi*radius*radius and radius is Diameter divide by 2 
elif (shapeRoom == 2):
    while True:
        try:
            ceilingD= float(input("what is the diameter of the ceiling in feet?"))
            break
        except ValueError:
            print("Please use numbers only")
    get_radius = ceilingD / 2
    circleA = round(float(math.pi * get_radius * get_radius),2)
    gallons_needed = math.ceil(circleA / gallon)
    print(f'You will need to purchase {gallons_needed} gallons of')
    print(f'paint to cover {circleA} square feet.')
elif (shapeRoom == 3):
    print("For this shape we will need 3 measurements, make sure to provide two of the longer sides and narrowest thank you")
    while True:
        try:
            lshapeA = float(input("First long measurement in feet?"))
            break
        except ValueError:
            print("Please use numbers only")

    while True:
        try:
            lshapeB = float(input("Second long measurement in feet?"))
            break
        except ValueError:
            print("Please use numbers only")

    while True:
        try:
            lshapeC = float(input("Narrowest measurement in feet?"))
            break
        except ValueError:
            print("Please use numbers only")
    smallA = lshapeA - lshapeC
    smallB = lshapeB - lshapeC
    lshapeArea = (lshapeA * lshapeC) + (smallB * lshapeC)
    gallons_needed = math.ceil(lshapeArea / gallon)
    print(f'You will need to purchase {gallons_needed} gallons of')
    print(f'paint to cover {lshapeArea} square feet.')
else:
    print('Invalid Input')
