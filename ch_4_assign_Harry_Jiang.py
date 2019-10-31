import math

class Point:
	x = 0
	y = 0
	distance = 0
	def __init__(self, x, y):
		self.x = x
		self.y = y

	#calculate distance
	def calculateDistance(self):
		return math.sqrt(self.x*self.x + self.y*self.y)

class Point_3D(Point):
	def __init__(self, x, y, z):
		super().__init__(x, y)
		self.z = z

	def calculateDistance(self):
		return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)



#aPoint = Point(1,1)
#print(aPoint.calculateDistance())
#aPoint = Point_3D(1, 1, 1)
#print(aPoint.calculateDistance())
IsInputValid = False
while IsInputValid == False:
	pointinput = input('please enter the value of two dimensional point\n')
	coordinate = pointinput.split(',')
	if not coordinate[0].isnumeric() or not coordinate[1].isnumeric():
		IsInputValid = False
	else:
		aPoint = Point(float(coordinate[0]), float(coordinate[1]))
		distance2D = aPoint.calculateDistance()
		print(distance2D)
		IsInputValid = True

Is3dInputValid = False
while Is3dInputValid == False:
	point3Dinput = input('please enter the value of the three dimensional point\n')
	coordinate3D = point3Dinput.split(',')
	if not coordinate3D[0].isnumeric() or not coordinate3D[1].isnumeric() or not coordinate3D[2].isnumeric():
		Is3dInputValid = False
	else:
		bPoint = Point_3D(float(coordinate3D[0]), float(coordinate3D[1]), float(coordinate3D[2]))
		distance3D = bPoint.calculateDistance()
		print(distance3D)
		Is3dInputValid = True

if distance2D > distance3D:
	print('two dimensional point distance is larger')
elif distance3D == distance2D:
	print('two dimensional point and three dimensional point distance are equal')
else:
	print('three dimensional point distance is larger')



