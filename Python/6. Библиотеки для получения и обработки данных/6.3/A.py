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
            super().__init__(args[0][0], args[0][1])
        elif len(args) == 2:
            super().__init__(args[0], args[1])
