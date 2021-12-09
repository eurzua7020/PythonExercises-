#7 Area of a Rectangular Room
while True:
    try:
        roomL = float(input("what is the length of the room in feet?"))
        break
    except ValueError:
        print("Please use numbers only")
while True:
    try:
        roomW = float(input("what is the width of the room?"))
        break
    except ValueError:
        print("Please use numbers only")
roomA = roomL * roomW
#converting Squared feet to squared meters. Multiple the area by 0.09290304
import math
truncA = math.trunc(roomA)
metersqr = round((roomA * 0.09290304), 3)
#nexr we'll import MATH module to truncate roomA 
print(f'The area is {roomA} square feet')#without truncate 
print(f'The area is {truncA} square feet')#with truncate
print(f'{metersqr} square meters')
