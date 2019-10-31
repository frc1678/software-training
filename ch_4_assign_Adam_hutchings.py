import math #For mathy stuff
class Point():
	def __init__(self, x_coord, y_coord):
		self.x_coord = x_coord
		self.y_coord = y_coord

	def distance(self): #Distance
		return math.sqrt((float(self.x_coord) ** 2) + (float(self.y_coord) ** 2)) #Pythagorean calculation

class Point_3D(Point): #Defining it for 3D
	def __init__(self, x_coord, y_coord ,z_coord):
		super().__init__(x_coord,y_coord)
		self.z_coord = z_coord

	def distance(self): #For 3D distance
		return math.sqrt((super().distance()**2) + (float(self.z_coord)**2))

def distance_counter(user_x_1,user_y_1,user_x_2,user_y_2,user_z):
	hypotenuse_2D = Point(user_x_1,user_y_1).distance() #So I can use it more efficiently later.
	hypotenuse_3D = Point_3D(user_x_2,user_y_2,user_z).distance() #So I can use it more efficiently later.
	print("Your first point is " + str(hypotenuse_2D) + '.')
	print("Your second point is " + str(hypotenuse_3D)+'.')

	if hypotenuse_3D > hypotenuse_2D:
		print("Your second point was further away. ")
	elif hypotenuse_3D == hypotenuse_2D:
		print("Your points tied. ")
	else:
		print("Your first point was further away. ")

def is_float(user_input): #Idiotproofing!
	for character in user_input:
		if character not in '0123456789.':
			return False
	if user_input is '':
		return False
	elif user_input.split().count(".") > 1:
		return False
	return True

while True:
	user_x_1 = input("What would you like your first 2D variable to be? ")
	user_x_2 = input("What would you like your second 2D variable to be? ")
	user_y_1 = input("What would you like your first 3D variable to be? ")
	user_y_2 = input("What would you like your second 3D variable to be? ")
	user_z = input("What would you like your third 3D variable to be? ")

	if is_float(str(user_x_1)) and is_float(str(user_x_2)) and is_float(str(user_y_1)) and is_float(str(user_y_2)) and is_float(str(user_z)) == True:
		break;
	else:
		print("Uh-oh, you messed up! ")
distance_counter(user_x_1, user_x_2, user_y_1, user_y_2, user_z)