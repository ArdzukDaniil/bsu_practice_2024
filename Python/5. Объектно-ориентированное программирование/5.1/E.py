class Rectangle:
    def __init__(self, corner1, corner2):
        self.x1, self.y1 = corner1
        self.x2, self.y2 = corner2

    def perimeter(self):
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        return round(2 * (width + height), 2)

    def area(self):
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        return round(width * height, 2)
