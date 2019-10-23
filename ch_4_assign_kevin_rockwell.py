from math import hypot

class Point():
    def __init__(self, x, y):
        self.x, self.y = x, y

    def distance(self):
        return hypot(self.x, self.y)


class Point_3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self):
        return hypot(super().distance(), self.z)


def get_num():
    while True:
        i = input("Enter a real number: ")
        sign = ""
        if i[0] in ["+", "-"]: # Has a sign as first value
            sign = i[0]
            i = i[1:] #Number without the sign
        decimal = False # Used to track if we've had a decimal point
        for c in i:
            if c not in "1234567890":
                if c == "." and not decimal:
                    decimal = True
                else:
                    print(f"Invalid input {i}")
                    break
        else:
            return float(sign + i)

if __name__ == "__main__":
    print("Enter x value for first point")
    x = get_num()
    print("Enter y value for first point")
    y = get_num()
    two_d = Point(x, y)
    print("Enter x value for second point")
    x = get_num()
    print("Enter y value for second point")
    y = get_num()
    print("Enter z value for second point\n")
    z = get_num()
    three_d = Point_3D(x, y, z)


    if two_d.distance() > three_d.distance():
        print("The first point is further from the origin")
    elif two_d.distance() < three_d.distance():
        print("The second point is further from the origin")
    else:
        print("The two points are equally far from the origin")

    if two_d.distance() > Point.distance(three_d): #Point to only use x and y
        print("The second point is further from origin in x and y")
    elif two_d.distance() < Point.distance(three_d):
        print("The first point is further from origin in x and y")
    else:
        print("The two points are equally far from the origin in x and y")
