import pytest

l = [0, 1, 2, 5, 6, 7]

@pytest.mark.parametrize("test_input,expected", [("l[3:]", [5,6,7]), ("l[:3]", [0,1,2]), ("l[2:4]", [2,5])])
def test_list_1(test_input, expected):
    assert eval(test_input)==expected

def test_list_2():
    assert l.__len__() == 6

def test_list_3():
    assert l.index(5)==3

def test_list_4():
    assert l.count(6)==1

def test_list_5():
    assert l.copy()==[0, 1, 2, 5, 6, 7]

