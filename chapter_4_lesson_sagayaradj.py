user_question_x_point_x = int(input('Type value for x for point x.'))
user_question_y_point_x = int(input('Type value for y for point x.'))
user_question_x_point_y = int(input('Type value for x for point y.'))
user_question_y_point_y = int(input('Type value for y for point y.'))
user_question_x_point_z = int(input('Type value for x for point z.'))
user_question_y_point_z = int(input('Type value for y for point z.'))
user_question_z_point_z = int(input('Type value for z for point z.'))
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self):
        import math
        print(math.sqrt(self.x**2 + self.y**2))
x = Point(user_question_x_point_x,user_question_y_point_x)
y = Point(user_question_x_point_y,user_question_y_point_y)
class Point_3D(Point):
        def __init__(self, x, y, z):
            super().__init__(x, y)
            self.z = z
        def distance_3D(self):
            import math
            print(math.sqrt(self.x**2 + self.y**2 + self.z**2))
x = Point_3D(user_question_x_point_z,user_question_y_point_z,user_question_z_point_z)
x.distance_3D()
user_points_question = input("Which 2D point would you like to use to find the distance from the 3D point, 'x' or 'y'")
print("act: " + str(user_points_question))
if user_points_question == 'x':
    user_points_question = True;
    def pointComparisons_x():
            if x<z == True:
                print("point x is less than point z")
            if x>z == True:
                print("point x is greater than point z")
            if x==z == True:
                print("point x and point z are equal")
if user_points_question == 'y':
    user_points_question = True;
    def pointComparisons_y():
            if y<z == True:
                print("point y is less than point z")
            if y>z == True:
                print("point y is greater than point z")
            if y==z == True:
                print("point y and point z are equal")


