import pytest
import sys
sys.path.append(".")
from triangle import Triangle
from figure import Figure


T = Triangle('little triangle', 20, 30, 40)
F = Figure('test figure')


def test_triangle_area():
    assert T.area == 45


def test_triangle_perimeter():
    assert T.perimeter == 90


def test_triangle_angles():
    assert T.angles == 3


def test_triangle_name():
    assert T.name == 'little triangle'


def test_triangle_figure_addition():
    F.area = 20
    assert T.add_square(F) == 65

