from math import sqrt
import math
def number_validation(number):
	return number.isdigit()

class Point_2D:
	x = 0
	y = 0
	distance = 0
	def __init__(self, x, y):
		self.x = x
		self.y = y	
	def distance(self):
		return sqrt(math.pow(int(self.x), 2) + math.pow(int(self.y), 2))

x = input("What is your 2D x value?\n")
while number_validation(x) == False:
	print("I'm sorry, please input an integer\n")
	x = input("What is your 2D x value?\n")
y = input("What is your 2D y value?\n")
while number_validation(y) == False:
	print("I'm sorry, please input an integer\n")
	y = input("What is your 2D y value?\n")

point_2D = Point_2D(x, y)
print("The distance of your two points from the origin " + str(point_2D.distance()))

class Point_3D(Point_2D):
	def __init__(self, x, y, z):
		super().__init__(x, y)
		self.z = z
	def distance(self):
		return sqrt(math.pow(int(self.x), 2) + math.pow(int(self.y), 2) + math.pow(int(self.z), 2))
	def distance_2D(self):
		return super().distance()

x = input("\nWhat is your 3D x value?\n")
while number_validation(x) == False:
	print("I'm sorry, please input an integer\n")
	x = input("What is your 3D x value?\n")
y = input("What is your 3D y value?\n")
while number_validation(y) == False:
	print("I'm sorry, please input an integer\n")
	y = input("What is your 3D y value?\n")
z = input("What is your 3D z value?\n")
while number_validation(z) == False:
	print("I'm sorry, please input an integer\n")
	z = input("What is your 3D z value?\n")

point_3D = Point_3D(x, y, z)
print("The distance of your three points from the origin is " + str(point_3D.distance()))

if point_2D.distance() > point_3D.distance():
	print("\nThe 2D point is farther from the origin than the 3D point\n")
elif point_2D.distance() < point_3D.distance():
	print("\nThe 3D point is farther from the origin than the 2D point\n")
elif point_2D.distance() == point_3D.distance():
	print("\nThe two points are the same distance from the origin\n")

if point_2D.distance() > point_3D.distance_2D():
	print("The x and y cooridnate of the 2D point are farther than that of the 3D point\n")
elif point_2D.distance() < point_3D.distance_2D():
	print("The x and y cooridnate of the 3D point are farther than that of the 2D point\n")
elif point_2D.distance() == point_3D.distance_2D():
	print("The x and y cooridnates of the 2D and 3D points are of equal distance")