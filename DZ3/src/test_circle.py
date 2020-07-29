import pytest
import sys
sys.path.append(".")
from circle import Circle
from figure import Figure
from rectangle import Rectangle


C = Circle('big circle', 60)
F = Figure('test figure')
R = Rectangle('test rectangle', 10, 20)


def test_circle_area():
    assert C.area > 11309
    assert C.area < 11310


def test_circle_perimeter():
    assert C.perimeter > 376
    assert C.perimeter < 377


def test_circle_angles():
    assert C.angles == 0


def test_circle_name():
    assert C.name == 'big circle'


def test_circle_figure_addition():
    F.area = 20
    a = C.add_square(F)
    assert a > 11329
    assert a < 11330


def test_circle_rectangle_addition():
    a = C.add_square(R)
    assert a > 11509
    assert a < 11510
