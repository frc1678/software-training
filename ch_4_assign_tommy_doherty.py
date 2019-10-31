from math import sqrt  #imports math and square root
import math

def number_validation(number):  #validation 
	return number.isdigit()

class Point3D:  #3D point class
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	def distance(self):
		d = (sqrt(math.pow(int(self.x), 2) + math.pow(int(self.y), 2) + math.pow(int(self.z), 2)))
		return d

class Point2D:  #2D point class
	def __init__(self, x_1, y_1,):
		self.x_1 = x_1
		self.y_1 = y_1
	def distance(self):
		d_1 = (sqrt(math.pow(int(x_1), 2) + math.pow(int(y_1), 2)))
		return d_1

x = input('What is your x value? ')  #takes input for 3D point
while not number_validation(x):
	print('not valid')
	x = input('What is your x value? ')
y = input('What is your y value? ')
while not number_validation(y):
	print('not valid')
	y = input('What is your y value? ')
z = input('What is your z value ')
while not number_validation(z):
	print('not valid')
	z = input('What is your z value ')

p = Point3D(x, y, z)  #prints 3D distance
print(p.distance())

x_1 = input('What is your x value for the 2D distance? ')  #takes 2D input
while not number_validation(x_1):
	print('not valid')
	x_1 = input('What is your x value for the 2D distance? ')
y_1 = input('What is your y value for the 2D distance? ')
while not number_validation(y_1):
	print('not valid')
	y_1 = input('What is your y value for the 2D distance? ')

print('your 2D point is')  #prints 2D point
p_1 = Point2D(x_1, y_1)
print(p_1.distance())

if p.distance() > p_1.distance():								#determines which point is longer
	print('The 3D distance is larger than the 2D point')
else:
	print('The 2D distance is larger than the 3D point')
if p.distance() == p_1.distance():
	print('The distances are equal')
if (sqrt(math.pow(int(x_1), 2) + math.pow(int(y_1), 2))) > (sqrt(math.pow(int(x), 2) + math.pow(int(y), 2))):	#prints which xy distance is furthest
	print('The 2D x,y is further away from the orgin than the 3D points x,y')
else:
	print('The 3D x,y is further away from the orgin than the 2D points x,y')
