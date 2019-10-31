import math

class Distanceorigin:
    def __init__ (self, xx, yy):
        self.newthing = xx
        self.y = yy
    def distance():
        #dist from origin is py theorm : w/ 0,0
      #  partone = x - 0
        partone = newthing - 0
        partwo = y - 0
        calculate = partone**2 + partwo**2
        lastpart = math.sqrt(calculate)
        print("The distance from the origin is: ")
        print(lastpart)
        return lastpart
class ThreeD:
    def __init__ (self, tdx, tdy, tdz):
        self.tx = tdx
        self.ty = tdy
        self.tz = tdz
    def distance():
        partone = tx**2 + ty**2 + tz**2
        parttwo = math.sqrt(partone)
        print("The distance from the origin is: ")
        print(parttwo)
        return parttwo

check = False
while check == False:
    x = input("What is the x cordinate? ")
    ycord = input("What is the y cordinate? ")
    if x.isdigit() and ycord.isdigit():
        newthing = float(x)
        y = float(ycord)
        check = True
a = int(Distanceorigin.distance())

checktwo = False
while checktwo == False:
    threedx = input("What is the x value of the 3D point? ")
    threedy = input("What is the y value of the 3D point? ")
    threedz = input("What is the z value of the 3D point? ")
    if threedx.isdigit() and threedy.isdigit() and threedz.isdigit():
        tx = int(threedx)
        ty = int(threedy)
        tz = int(threedz)
        checktwo = True

b = int(ThreeD.distance())
def comparison(a, b):
    if a > b:
        print("The 2D point is farther from the origin")
    if a < b:
        print("The 3D point is farther from the origin")
comparison(a, b)
