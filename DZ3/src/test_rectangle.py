import pytest
import sys
sys.path.append(".")
from rectangle import Rectangle
from figure import Figure


R = Rectangle('rectangle', 20, 30)
F = Figure('test figure')


def test_rectangle_area():
    assert R.area == 600


def test_rectangle_perimeter():
    assert R.perimeter == 100


def test_rectangle_angles():
    assert R.angles == 4


def test_rectangle_name():
    assert R.name == 'rectangle'


def test_rectangle_figure_addition():
    F.area = 200
    assert R.add_square(F) == 800

