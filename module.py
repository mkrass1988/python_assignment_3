from math import pi

def house_sq_ft(x,y):
    area = int(x) * int(y)
    print("The area is " + str(area) + " square feet")

def circumference(r):
    circ = 2 * pi * int(r)
    print("The circumference is " + str(circ))