import pytest
import requests


@pytest.mark.parametrize("test_input,expected", [("r.status_code", 200), ("len(j) == 100", True)])
def test_get_posts(test_input, expected):
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    j = r.json()
    assert eval(test_input) == expected


def test_delete_post():
    r = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
    assert r.status_code == 200


@pytest.mark.parametrize("test_input,expected", [("r.status_code", 200), ("len(j) == 500", True)])
def test_get_comments(test_input, expected):
    r = requests.get('https://jsonplaceholder.typicode.com/comments')
    j = r.json()
    assert eval(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("r.status_code", 201), ("len(j) > 0", True)])
def test_post_comment(test_input, expected):
    r = requests.post('https://jsonplaceholder.typicode.com/comments', 'id=2&title="alert!"&body="injection"&userID=1')
    j = r.json()
    assert eval(test_input) == expected


def test_get_albums():
    r=requests.get('https://jsonplaceholder.typicode.com/albums')
    assert r.status_code == 200
    j = r.json()
    assert len(j) == 100


def test_get_photos():
    r=requests.get('https://jsonplaceholder.typicode.com/photos')
    assert r.status_code == 200
    j = r.json()
    assert len(j) == 5000


def test_get_users():
    r=requests.get('https://jsonplaceholder.typicode.com/users')
    assert r.status_code == 200
    j = r.json()
    assert len(j) == 10
