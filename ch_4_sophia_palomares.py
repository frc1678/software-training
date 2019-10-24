from math import sqrt

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distance(self):
		self.distance_solve = sqrt(self.x**2 + self.y**2)
		return self.distance_solve

class Point3D(Point):
	def __init__(self, x, y, z):
		super().__init__(x, y)
		self.z = z

	def distance(self):
		self.distance_3D_solve = sqrt(super().distance()**2 + self.z**2)
		return self.distance_3D_solve

def distance_maker():
	print("you are finding the hypotonuse of a 2D triangle")
	x_input = input("What is the x value? ")
	x_input = validation(x_input)
	y_input = input("what is the y value? ")
	y_input = validation(y_input)
	hyp = Point(x_input, y_input)
	return hyp

def distance_maker_3D():
	print("you are finding the hypotonuse of a 3D triangle")
	x_input = input("What is the x value? ")
	x_input = validation(x_input)
	y_input = input("what is the y value? ")
	y_input = validation(y_input)
	z_input = input("What is the z value? ")
	z_input = validation(z_input)
	hyp_3D = Point3D(x_input, y_input, z_input)
	return hyp_3D

def checker():
	p1 = distance_maker()
	print("This is the hypotenuse for the 2D triangle")
	print(p1.distance())
	p2 = distance_maker_3D()
	print("This is the hypotenuse for the 3D triangle")
	print(p2.distance())
	if p1.distance() > p2.distance():
		print("2D-hypotenuse is bigger")
	elif p1 == p2:
		print("The hypotenuses are equal")
	else:	
		print("3D-hypotenuse is bigger")

def validation(user_input):
	if user_input.isdigit():
		user_input = int(user_input)
		return user_input
	else:
		print("Input wasn't a number, please enter a number.")
		user_new_input = input("Please enter a value: ")
		validation(user_new_input)

checker()