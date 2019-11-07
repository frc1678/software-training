import math 
class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def dist(self):
        return math.sqrt(self.x**2 + self.y**2)

class Point3D(Point):
    def __init__ (self, x, y, z):
        super().__init__ (x, y)
        self.z = z
    def dist(self):
        return math.sqrt((super().dist())**2 + self.z**2)

class Determine(Point3D):
    def __init__(self, x2D, y2D, x, y, z):
        super().__init__ (x, y, z)
        self.x2D = x2D
        self.y2D = y2D
    def compare_tot_dist(self):
        if super().dist() > Point(self.x2D, self.y2D).dist():
            return "3D point is farther from the origin."
        elif super().dist() == Point(self.x2D, self.y2D).dist():
            return "Points are equidistant from origin."
        else:
            return "2D point is farther from origin."
def check_if_int(a):
    while True:
        if a == 'quit':
            return None
        elif a.isdigit() == True:
            a = int(a)
            return a
        else:
            a = input("Please type value as an integer: ")


x = input("What is the x coordinate of the 2D point? ")
x = check_if_int(x)

y = input("What is the y coordinate of the 2D point? ")
y = check_if_int(y)

point_2D = Point(x, y)
dist_2D = point_2D.dist()
print(dist_2D)


x3D = input("What is the x coordinate of the 3D point? ")
x3D = check_if_int(x3D)

y3D = input("What is the y coordinate of the 3D point? ")
y3D = check_if_int(y3D)

z = input("What is the z coordinate of the 3D point? ")
z = check_if_int(z)

point_3D = Point3D(x3D, y3D, z)
dist_3D = point_3D.dist()
print(dist_3D)

compare = Determine(x, y, x3D, y3D, z)
dist_tot_compare = compare.compare_tot_dist()
print(dist_tot_compare)







