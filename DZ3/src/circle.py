import sys
sys.path.append(".")
from figure import Figure


class Circle(Figure):
    def __init__(self, name, r):
        self.area = 0
        self.angles = 0
        self.perimeter = 0
        self.r = r
        self.pi = 3.14159265
        super().__init__(name)

    def get_angles(self):
        self.angles = 0
        return self.angles

    def get_perimeter(self):
        self.perimeter = self.pi*self.r*2
        return self.perimeter

    def get_area(self):
        self.area = self.pi*self.r*self.r
        return self.area

