import pytest

s = {0, 1, 2, 5, 6, 7}

@pytest.mark.parametrize("test_input,expected", [("s & {0, 1}", {0, 1}), ("s | {3, 4}", {0, 1, 2, 3, 4, 5, 6, 7})])
def test_set_1(test_input, expected):
    assert eval(test_input)==expected

def test_set_2():
    assert s.__len__()==6

def test_set_3():
    assert s.difference({3, 4, 5, 6})=={0, 1, 2, 7}

def test_set_4():
    assert s.issuperset({6, 7})==True

def test_set_5():
    assert s.copy()=={0, 1, 2, 5, 6, 7}

