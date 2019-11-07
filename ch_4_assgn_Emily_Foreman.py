import math

class Two_D_Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def distance():
        #dist from origin is py theorm : w/ 0,0
      #  partone = x - 0
        part_one_calculation = x - 0
        part_two_calculation = y - 0
        calculate = part_one_calculation**2 + part_two_calculation**2
        lastpart = math.sqrt(calculate)
        print("The distance from the origin is: ")
        print(lastpart)
        return lastpart
class ThreeD(Two_D_Point):
    def __init__ (self, x, y,z):
        self.z = tdz
    def distance():
        part_one_calculation =x**2 + y**2 + z**2
        part_two_calculation = math.sqrt(part_one_calculation)
        print("The distance from the origin is: ")
        print(part_two_calculation)
        return part_two_calculation

check = False
while check == False:
    x = input("What is the x cordinate? ")
    y = input("What is the y cordinate? ")
    if x.isdigit() and y.isdigit():
        x = float(x)
        y = float(y)
        check = True
Distance  = int(Two_D_Point.distance())
checktwo = False
while checktwo == False:
    TDx = input("What is the x value of the 3D point? ")
    TDy = input("What is the y value of the 3D point? ")
    TDz = input("What is the z value of the 3D point? ")
    if TDx.isdigit() and TDy.isdigit() and TDz.isdigit():
        x = int(TDx)
        y = int(TDy)
        z = int(TDz)
        checktwo = True

ThreeD_Distance = int(ThreeD.distance())
def comparison(Distance, ThreeD_Distance):
    if Distance > ThreeD_Distance:
        print("The 2D point is farther from the origin")
    elif Distance < ThreeD_Distance:
        print("The 3D point is farther from the origin")
    elif Distance == ThreeD_Distance:
        print("The points are equal in distance")
comparison(Distance, ThreeD_Distance)
