class Bot():

    def __init__(self, pos, name):
        self.name = name
        self.pos = pos
        self.arm = 0
        self.cube = False
    def roll(self, distance):
        self.pos = self.pos + distance
    def armMove(self, distance):
        self.arm = self.arm + distance
    def pick(self):
        if self.pos == 3:
            self.cube = True
Rob = Bot(0, "Rob")
while True:
    print("Robot is at pos " + str(Rob.pos) + " with arm pos " + str(Rob.arm) + " and cube is " + str(Rob.cube))
    func = input("cube, roll, armMove?")
    if func == "cube":
        Rob.pick()
    elif func == "armMove":
        Rob.armMove(1)
    elif func == "roll":
        Rob.roll(1)
    