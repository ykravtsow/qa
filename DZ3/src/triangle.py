import sys
sys.path.append(".")
from figure import Figure


class Triangle(Figure):
    def __init__(self, name, a, b, c):
        self.area = 0
        self.angles = 0
        self.perimeter = 0
        self.a = a
        self.b = b
        self.c = c
        super().__init__(name)

    def get_perimeter(self):
        self.perimeter = self.a+self.b+self.c
        return self.perimeter

    def get_area(self):
        self.area = self.get_perimeter()/2
        return self.area

    def get_angles(self):
        self.angles = 3
        return self.angles


