from math import sqrt;
import math;

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
		print(super().calculateDistance())
		print(self.z**2)
		return math.sqrt(super().calculateDistance() + self.z**2)

x = int(input('what is the x value\n'))
y = int(input('what is the y value\n'))
aPoint = Point( float(x), float(y))
distance2D = aPoint.calculateDistance()

print(distance2D)

x = int(input('what is the 3D x value\n'))
y = int(input('what is the 3D y value\n'))
z = int(input('what is the 3D z value\n'))
bPoint = Point3D( float(x), float(y), float(z))
distance3D = bPoint.calculateDistance()

print(distance3D)

if distance2D>distance3D:
	print('the 2d distance point is farther\n')
elif distance3D == distance2D:
	print('the two points are equally far from origin\n')
else:
	print('the 3d distance point is farther\n')