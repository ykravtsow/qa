from abc import abstractmethod


class Figure:
    def __init__(self, name):
        self.name = name
        self.angles = self.get_angles()
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()

    def add_square(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError('Wrong class object given')

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_angles(self):
        pass
