from math import sqrt;
import math;

def number_validation(number):
    return number.isdigit()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def calculateDistance(self):
        return math.sqrt(self.x**2 + self.y**2)

class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y) 
        self.z = z
    def calculateDistance(self):
        return math.sqrt(super().calculateDistance() + self.z**2)

x = input('what is the x value\n')
while number_validation(x) == False:
    print('not valid')
    x = input('what is the x value')
y = input('what is the y value\n')
while number_validation(y) == False:
    print('not valid')
    y = input('what is your 2d y value')
aPoint = Point( float(x), float(y))
distance2D = aPoint.calculateDistance()

print(distance2D)

x = input('what is the 3D x value\n')
while number_validation(x) == False:
    print('not valid')
    x = input('what is your 3D x value\n')
y = input('what is the 3D y value\n')
while number_validation(y) == False:
    print('not valid')
    y = input('what is your 3D y value\n')
z = input('what is the 3D z value\n')
while number_validation(z) == False:
    print('not valid')
    z = input('what is your z value\n')
bPoint = Point3D( float(x), float(y), float(z))
distance3D = bPoint.calculateDistance()

print(distance3D)

if distance2D>distance3D:
    print('the 2d distance point is farther\n')
elif distance3D == distance2D:
    print('the two points are equally far from origin\n')
else:
    print('the 3d distance point is farther\n')