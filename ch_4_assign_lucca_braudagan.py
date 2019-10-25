from math import sqrt

class Point:
	def __init__(self, x_value, y_value):
		self.x_value = x_value
		self.y_value = y_value

	def distance(self):
		return sqrt(x_value ** 2 + y_value ** 2)

class Point_3D(Point):
	def __init__(self, x_value, y_value, z_value):
		super().__init__(x_value, y_value)
		self.z_value = z_value

	def distance(self):
		distance_2D = super().distance()
		return sqrt(distance_2D ** 2 + z_value ** 2)

def int_validation(prompt):
	while True:
		if prompt.isdigit():
			return int(prompt)
		else:
			prompt = input("This is not a valid number. Try again. ")

x_value_2D = input("What is the x-value of your 2D point? ")
x_value = int_validation(x_value_2D)

y_value_2D = input("What is the y-value of your 2D point? ")
y_value = int_validation(y_value_2D)

point_2D = Point(x_value, y_value)
point_2D_distance = point_2D.distance()

x_value_3D = input("What is the x-value of your 3D point? ")
x_value = int_validation(x_value_3D)

y_value_3D = input("What is the y-value of your 3D point? ")
y_value = int_validation(y_value_3D)

z_value_3D = input("What is the z-value of your 3D point? ")
z_value = int_validation(z_value_3D)

point_3D = Point_3D(x_value, y_value, z_value)

point_3D_distance = point_3D.distance()

if point_2D_distance > point_3D_distance:
	print(point_2D_distance)
	print("is greater than")
	print(point_3D_distance)
	print("The distance of the 2D point in farther from the origin than the 3D point.")

elif point_2D_distance < point_3D_distance:
	print(point_2D_distance)
	print("is less than")
	print(point_3D_distance)
	print("The distance of the 2D point in closer to the origin than the 3D point.")

elif point_2D_distance == point_3D_distance:
	print(point_2D_distance)
	print("is equal to")
	print(point_3D_distance)
	print("The 2D point and 3D point are equal distance from the origin.")

else:
	print("Something went wrong. The 2D point distance is not greater than, less than, or equal to the 3D point distance from the origin.")






