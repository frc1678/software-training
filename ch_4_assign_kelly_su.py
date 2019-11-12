from math import sqrt;
import math;
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def distance_2D (self):
		return float(sqrt(math.pow(int(self.x), 2) + math.pow(int(self.y),2)))

while True:
	x = input("Please enter your 2D x value.\n==>")
	if (x.isdigit()):
		break
	else: 
		print("Invalid input.")

while True:
	y = input("Please enter your 2D y value.\n==>")
	if (y.isdigit()):
		break
	else:
		print("Invalid input.")
		

point_one = Point(x, y)
print("The distance is " + str(point_one.distance_2D()) + "\n")

class Point_3D(Point):
	def __init__(self, x, y, z):
		super().__init__(x, y)
		self.z = z
	def distance_3D(self):
		return float(sqrt(math.pow(int(self.x), 2) + math.pow(int(self.y), 2) + math.pow(int(self.z), 2)))
	def distance_2D(self):
		return super().distance_2D()

while True:
	x = input("Please enter your 3D x value.\n==>")
	if (x.isdigit()):
		break
	else:
		print("Invalid input.")

while True:
	y = input("Please enter your 3D y value.\n==>")
	if (y.isdigit()):
		break
	else:
		print("Invalid input.")

while True:
	z = input("Please enter your 3D z value.\n==>")
	if (z.isdigit()):
		break
	else:
		print("Invalid input.")

point_two = Point_3D(x, y, z)
print("The distance is " + str(point_two.distance_3D()) + "\n")

if (point_one.distance_2D()) > (point_two.distance_3D()):
	print("The 2D point is furthest from the origin.")
elif (point_one.distance_2D()) < (point_two.distance_3D()):
	print("The 3D point is furthest from the origin.")
elif (point_one.distance_2D()) == (point_two.distance_3D()):
	print("The 2D and 3D point have equally furthest from the origin.")

if (point_one.distance_2D()) > (point_two.distance_2D()):
	print("The 2D point has x and y coordinates furthest from the origin.")
elif (point_one.distance_2D()) < (point_two.distance_2D()):
	print("The 3D point has x and y coordinates furthest from the origin.")
elif (point_one.distance_2D()) == (point_two.distance_2D()):
	print("The 2D and 3D x and y coordinates have equal values.")



