from math import sqrt

class Point:
	def __init__(self, x_value, y_value):
		self.x_value = x
		self.y_value = y

	def distance(self):
		return sqrt(x ** 2 + y ** 2)

class Point_3D(Point):
	def __init__(self, x_value, y_value, z_value):
		super().__init__(x, y)
		self.z_value = z

	def distance(self):
		distance_2D = super().distance()
		return sqrt(distance_2D ** 2 + z ** 2)

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


x_value_3D = input("What is the x-value of your 3D point? ")
x_value = int_validation(x_value_3D)

y_value_3D = input("What is the y-value of your 3D point? ")
y_value = int_validation(y_value_3D)

z_value_3D = input("What is the z-value of your 3D point? ")
z_value = int_validation(z_value_3D)

