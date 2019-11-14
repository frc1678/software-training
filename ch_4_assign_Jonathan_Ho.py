from math import sqrt

# 2D Pythagorean Theorem
class Point():
	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)

	# Pythagorean Theorem
	def Distance(self):
		hypo = self.x ** 2 + self.y ** 2
		return sqrt(hypo)

# Three Dimensional Pythagorean Theorem
class Point_3D(Point):
	def __init__(self, x, y, z):
		self.z = float(z)
		super().__init__(x, y)
		

	def Distance(self):
		hypo_2 = super().Distance() ** 2 + self.z ** 2	
		return sqrt(hypo_2)

while True:
	Operation = input("What type of dimension do you want to use for the Pythagorean Theorem? If you wish to leave, type 'exit'.")
	if Operation == "2D":
		x = input("Enter the first value of your first leg of your triangle.")
		y = input("Enter the second value of your next leg.")
		# Assure if x and y are integers
		if x.isdigit() and y.isdigit():
			point = Point(x, y).Distance()
			print(point)
		else:
			print("Sorry, the variable is not a number. Try again.")
	
	elif Operation == "3D":
		x = input("Enter the first value of the length of the side of your 3D rectangle.")
		y = input("Enter the next value of the second length of your 3D rectangle.")
		z = input("Now enter the height of your 3D rectangle")
		# Validates if the inputs are integers for the code to use the if statement
		if x.isdigit() and y.isdigit() and z.isdigit():
			calc_3D_point = Point_3D(x, y, z).Distance()
			print(calc_3D_point)
		else:
			print("Sorry, your variable wasn't an integer. Try using a number.")

	# If the user wants to compare 2D and 3D points
	elif Operation == "Origin":
		# 2D
		x = input("Enter the first value of your first leg of your triangle.")
		y = input("Enter the second value of your next leg.")
		# Assure if x and y are integers
		if x.isdigit() and y.isdigit():
			point = Point(x, y)
			print(point)
		else:
			print("Sorry, the variable is not a number. Try again.")
		# 3D
		x2 = input("Enter the first value of the length of the side of your 3D rectangle.")
		y2 = input("Enter the next value of the second length of your 3D rectangle.")
		z2 = input("Now enter the height of your 3D rectangle")
		# Validates if the inputs are integers for the code to use the if statement
		if x2.isdigit() and y2.isdigit() and z2.isdigit():
			calc_3D_point = Point_3D(x2, y2, z2)
			print(calc_3D_point)
			if point.Distance() > calc_3D_point.Distance():
				print("The point farthest from the origin is: (" + str(x) + ", " + str(y) + ").")
			elif point.Distance() < calc_3D_point.Distance():
				print("The point farthest from the origin is: (" + str(x2) + ", " + str(y2) + ", " + str(z2) + ").")
			elif point.Distance() == calc_3D_point.Distance():
				print("My, my. The distance from the origin between those two coordinates are equal. How coincidential!")
			else: 
				print("Oops! I didn't get that. Try again.")
		else:
			print("Sorry, your variable wasn't an integer. Try using a number.")

	# If the user wishes to leave
	elif Operation == "exit":
		print("So long! Till we meet again.")
		break;
	# If the user types it incorrectly
	else:
		print("Sorry. Your response wasn't valid. Try 3D, 2D, or Origin.")
