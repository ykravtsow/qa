import requests
import pytest


@pytest.mark.parametrize("test_input,expected", [("r.status_code", 200), ("len(j['message']) > 0", True)])
def test_list_all_breeds(test_input, expected):
    r = requests.get('https://dog.ceo/api/breeds/list/all')
    j = r.json()
    assert eval(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("r.status_code", 200), ("len(j['message']) > 0", True)])
def test_by_breed(test_input, expected):
    r = requests.get('https://dog.ceo/api/breed/hound/images')
    j = r.json()
    assert eval(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("r.status_code", 200), ("j['status']", "success")])
@pytest.mark.parametrize("breed", ["hound", "bulldog", "dingo", "spaniel"])
def test_by_sub_breed(breed, test_input, expected):
    r = requests.get('https://dog.ceo/api/breed/' + breed + '/list')
    j = r.json()
    assert eval(test_input) == expected


def test_random_image():
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    j = r.json()
    assert j['status'] == 'success'


@pytest.mark.parametrize("test_input", ["hound", "bulldog", "dingo", "spaniel"])
def test_breeds_list(test_input):
    r = requests.get('https://dog.ceo/api/breed/' + test_input + '/images/random')
    j = r.json()
    assert (j['message'] != "") and (j['message'])

