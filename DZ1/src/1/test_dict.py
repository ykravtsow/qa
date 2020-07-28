import pytest

d = {"test1" : "012567", "test2" : [0,1,2,5,6,7], "test3" : {0, 1, 2, 5, 6, 7}}

@pytest.mark.parametrize("test_input,expected", [("d['test1']", "012567"), ("d['test2']", [0,1,2,5,6,7])])
def test_dict_1(test_input, expected):
    assert eval(test_input)==expected

def test_dict_2():
    assert d.__len__()==3

def test_dict_3():
    assert set(d.keys())=={"test1", "test2", "test3"}

def test_dict_4():
    assert d.get("test2", "")==[0,1,2,5,6,7]

def test_dict_5():
    assert d.copy() == {"test1" : "012567", "test2" : [0,1,2,5,6,7], "test3" : {0, 1, 2, 5, 6, 7}}