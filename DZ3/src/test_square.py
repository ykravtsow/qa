import pytest
import sys
sys.path.append(".")
from square import Square
from figure import Figure


S = Square('my square', 40)
F = Figure('test figure')


def test_square_area():
    assert S.area == 1600


def test_square_perimeter():
    assert S.perimeter == 160


def test_square_angles():
    assert S.angles == 4


def test_square_name():
    assert S.name == 'my square'


def test_square_figure_addition():
    F.area = 2000
    assert S.add_square(F) == 3600

