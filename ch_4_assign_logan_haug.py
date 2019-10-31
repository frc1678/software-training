from math import sqrt
from isfloat import isfloat
class point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def origin(self):
        return round(sqrt((self.x ** 2 + self.y ** 2)))
    def isValid(self):
        return isfloat(self.x) and isfloat(self.y)
    def __str__(self):
        return str(self.x) + ", " + str(self.y)

class point3d(point):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z
    def origin(self):
        return super().origin() + (self.z ** 2)
    def isValid(self):
        return super().isValid and isfloat(self.z)
    def __str__(self):
        return super().__str__() + ", " + str(self.z)
user_2d = input("Enter two numbers seperated by spaces: ").split(" ")
user_3d = input("Enter three numbers seperated by spaces: ").split(" ")
if len(user_2d) != 2 or len(user_3d) != 3:
    print("why are you like this")
else:
    user_point = point(user_2d[0], user_2d[1])
    user_point3d = point3d(user_3d[0], user_3d[1], user_3d[2])
    if not user_point.isValid() or not user_point3d.isValid():
        print("why are you like this 2")
    else:
        user_point = point(float(user_2d[0]), float(user_2d[1]))
        user_point3d = point3d(float(user_3d[0]), float(user_3d[1]), float(user_3d[2]))
        if user_point.origin() == user_point3d.origin():
            print("The two dimensional coordinate's distance from the origin is equal to the three dimensional coordinate's distance from the origin'")

        elif user_point.origin() > user_point3d.origin():
            print(user_point)

        else:
            print(user_point3d)
