class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, shift_x, shift_y):
        self.x += shift_x
        self.y += shift_y

    def length(self, p):
        return round(((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if not args:
            super().__init__(0, 0)
        elif len(args) == 1 and isinstance(args[0], tuple):
            super().__init__(*args[0])
        elif len(args) == 2:
            super().__init__(*args)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"

    def __add__(self, other):
        return PatchedPoint(self.x + other[0], self.y + other[1])

    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]
        return self
