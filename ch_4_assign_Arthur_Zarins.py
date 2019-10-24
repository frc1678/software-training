import math
class BasicPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self):
        return math.sqrt(self.x **2 + self.y **2)
    
class AwesumPointz(BasicPoint):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self):
        return math.sqrt(self.z * self.z + math.sqrt(self.x **2 + self.y **2) **2)

boringPoint2d = BasicPoint(3, 4)
coolPoint = AwesumPointz(3, -4, 4)
print(boringPoint2d.distance())
print(coolPoint.distance())