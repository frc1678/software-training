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
            return math.sqrt(self.x **2 + self.y **2)
        else:
            return -1
    
class Point3d(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self):
        if (is_number(self.x) and is_number(self.y) and is_number(self.z)):
            return math.sqrt(self.z **2 + super().distance() ** 2)
        else:
            return -1

boringPoint2d = Point(3, 4)
coolPoint = Point3d(3, -4, 4)
wrong = Point3d("q", -4, 4)
print(boringPoint2d.distance())
print(coolPoint.distance())
print(wrong.distance())
#We know the last one's bogus because it's value is -1