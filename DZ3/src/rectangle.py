import sys
sys.path.append(".")
from figure import Figure


class Rectangle(Figure):
    def __init__(self, name, a, b):
        self.area = 0
        self.angles = 0
        self.perimeter = 0
        self.a = a
        self.b = b
        super().__init__(name)

    def get_angles(self):
        self.angles = 4
        return self.angles

    def get_perimeter(self):
        self.perimeter = self.a*2+self.b*2
        return self.perimeter

    def get_area(self):
        self.area = self.a*self.b
        return self.area

