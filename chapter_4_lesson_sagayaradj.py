user_question_x = int(input('Type value for x.'))
user_question_y = int(input('Type value for y.'))
user_question_z = int(input('Type value for z.'))
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, x, y):
        import math
        print(math.sqrt(self.x**2 + self.y**2))
x = user_question_x
y = user_question_y
class Point_3D(Point):
        def __init__(self, x, y, z):
            Point.__init__(self, x, y, z)
            self.z = z
        def distance(self, x, y, z):
            import math
            print(math.sqrt(self.x**2 + self.y**2 + self.z**2))
z = user_question_z
Point_3D.distance(user_question_x, user_question_y, user_question_z)
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


