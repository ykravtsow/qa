import pytest

s = "012567"

@pytest.mark.parametrize("test_input,expected", [("s[3:]", "567"), ("s[:3]", "012"), ("s[2:4]", "25")])
def test_string_1(test_input, expected):
    assert eval(test_input)==expected

def test_string_2():
    assert s.__len__() == 6

def test_string_3():
    assert s.index("5")==3

def test_string_4():
    assert s.count("6")==1

def test_string_5():
    assert s.split("2")==["01", "567"]
