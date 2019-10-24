
# Credits:
# Christopher Mowla for providing the function @ https://docs.google.com/file/d/0Bx0h7-zg0f4NTUM1MWUtaDJrbms/edit
# Arthur Zarins for compiling the code
import math


class cube():
    def __init__(self, size):
        self.size = size

    def combos(self):
        # 8 corners have 8 possibilities
        total = math.factorial(8) * (3 ** 7) / 24 ** ((self.size + 1) % 2)
        # add center edges
        total = total * ((math.factorial(12) * (2 ** 10)) ** (self.size % 2))
        # add wing edges
        total = total * (math.factorial(24) ** round((self.size - 2) / 2))
        # add centers
        total = total * ((math.factorial(24) / (math.factorial(4) ** 6))
                         ** round(((self.size - 2) / 2) ** 2))
        return total


myCube = cube(2)
print(myCube.combos())
