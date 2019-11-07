import math


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        if (is_number(self.x) and is_number(self.y)):
            return math.sqrt(float(self.x) ** 2 + float(self.y) ** 2)
        else:
            return -1


class Point3d(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self):
        if (is_number(self.x) and is_number(self.y) and is_number(self.z)):
            return math.sqrt(float(self.z) ** 2 + super().distance() ** 2)
        else:
            return -1


while True:
    a1 = input("give the x value of the 2d point \n")
    a2 = input("give the y value of the 2d point\n")
    a3 = input("give the x value of the 3d point\n")
    a4 = input("give the y value of the 3d point\n")
    a5 = input("give the z value of the 3d point\n")
    boringPoint2d = Point(a1, a2)
    coolPoint = Point3d(a3, a4, a5)

    if boringPoint2d.distance() == -1:
        print("The 2d point has arguements that are not real numbers")
    if coolPoint.distance() == -1:
        print("The 3d point has arguements that are not real numbers")
    if boringPoint2d.distance() == coolPoint.distance():
        print("They have equal distances")
    if boringPoint2d.distance() > coolPoint.distance():
        print("The 2d point's furthur away from the orgin")
    elif boringPoint2d.distance() < coolPoint.distance():
        print("The 3d point's furthur away from the orgin")
    print("The distance from the 2d point to orgin: " +
          str(boringPoint2d.distance()))
    print("The distance from the 3d point to orgin: " + str(coolPoint.distance()))
            
