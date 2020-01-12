import math
class Points:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def Distance(self):
        return float(math.sqrt((self.x ** 2) + (self.y ** 2)))

class Points_3D(Points):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def Distance_3D(self):
        return float(math.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2)))
while 0 == 0:
    activated = "On"
    while activated == 'On':
        validation_1_x = input('What is the x value of Point 1?: ')
        validation_1_y = input('What is the y value of Point 1?: ')
        validation_2_x = input('What is the x value of Point 2?: ')
        validation_2_y = input('What is the y value of Point 2?: ')
        validation_2_z = input('What is the z value of Point 2?: ')
        try:
            point_1_x = float(validation_1_x)
        except:
            print("Only intergers are allowed.")
            activated = 'Off'
        try:
            point_1_y = float(validation_1_y)
        except:
            print("Only intergers are allowed.")
            activated = 'Off'
        try:
            point_2_x = float(validation_2_x)
        except:
            print("Only intergers are allowed.")
            activated = 'Off'
        try:
            point_2_y = float(validation_2_y)
        except:
            print("Only intergers are allowed.")
            activated = 'Off'
        try:
            point_2_z = float(validation_2_z)
        except:
            print("Only intergers are allowed.")
            activated = 'Off'
        if activated == 'Off':
            print('You entered something that was not an interger. Please try again using only numbers.')
        else:
            point_1 = Points(point_1_x, point_1_y)
            point_2 = Points_3D(point_2_x, point_2_y, point_2_z)
            point_2_xy = Points(point_2_x, point_2_y)

            if point_1.Distance() > point_2.Distance_3D():
                print('Point 1 is further from the origin than Point 2, with a distance of ' + str(point_1.Distance()) + '.')
            elif point_2.Distance_3D() > point_1.Distance():
                print('Point 2 is further from the origin than Point 1, with a distance of ' + str(point_2.Distance_3D()) + '.')
            elif point_1.Distance() == point_2.Distance_3D():
                print('The points are the same distance from the origin, with a distance of ' + str(point_1.Distance()) + '.')
            if point_1.Distance() > point_2_xy.Distance():
                print('Point 1 is further from the origin on the xy axis than Point 2, with a distance of ' + str(point_1.Distance()) + '.')
            elif point_2_xy.Distance() > point_1.Distance():
                print('Point 2 is further from the origin on the xy axis than Point 1, with a distance of ' + str(point_2_xy.Distance()) + '.')
            elif  point_1.Distance() == point_2_xy.Distance():
                print('The points are the same distance from the origin on the xy axis, with a distance of ' + str(point_1.Distance()) + '.')