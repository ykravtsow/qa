import sys
sys.path.append(".")
from figure import Figure


class Square(Figure):
    def __init__(self, name, a):
        self.area = 0
        self.angles = 0
        self.perimeter = 0
        self.a = a
        super().__init__(name)

    def get_angles(self):
        self.angles = 4
        return self.angles

    def get_area(self):
        self.area = self.a*self.a
        return self.area

    def get_perimeter(self):
        self.perimeter = self.a*4
        return self.perimeter

