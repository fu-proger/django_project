class Point:
    def __init__(self, name, x, y):
        self.x = x
        self.y = y
        self.name = name

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return tuple([self.x, self.y])

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def __str__(self):
        return self.name + "(" + str(self.x) + ", " + str(self.y) + ")"