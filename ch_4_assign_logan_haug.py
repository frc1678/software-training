from math import fabs, sqrt
class coordinate_pair():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def origin(self):
        return round(sqrt((fabs(self.x) ** 2 + fabs(self.y) ** 2)))

class three_dee(coordinate_pair):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z
    def findOrigin(self):
        return sqrt((fabs(self.x) ** 2 + fabs(self.y) ** 2) + (fabs(self.z)**2))

user_2d = input("Enter two numbers seperated by spaces: ").split(" ")
user_3d = input("Enter three numbers seperated by spaces: ").split(" ")

converted_2d = []
converted_3d = []

if len(user_2d) != 2 and len(user_3d) != 3:
    print("Please enter the correct amount of numbers")

for convert in user_2d:
    if not convert.isnumeric():
        break
    converted_2d.append(float(convert))

for convert1 in user_3d:
    if not convert1.isnumeric():
        break
    converted_3d.append(float(convert))

if len(converted_2d) == 2 and len(converted_3d) == 3:

    if coordinate_pair(converted_2d[0], converted_2d[1]).origin() == three_dee(converted_3d[0],converted_3d[1],converted_3d[2]).findOrigin():
        print("The two dimensional coordinate's distance from the origin is equal to the three dimensional coordinate's distance from the origin'")

    elif coordinate_pair(converted_2d[0], converted_2d[1]).origin() > three_dee(converted_3d[0],converted_3d[1],converted_3d[2]).findOrigin():
        print(converted_2d)

    else:
        print(converted_3d)
        
else:
    print("Please enter only numbers")
