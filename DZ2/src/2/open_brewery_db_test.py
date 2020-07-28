import pytest
import requests


@pytest.mark.parametrize("test_input,expected", [("r.status_code", 200), ("len(j) > 0", True)])
def test_open_brewery_db_list_breweries(test_input, expected):
    r = requests.get('https://api.openbrewerydb.org/breweries')
    j = r.json()
    assert eval(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("r.status_code", 200), ("j['name'] != ''", True)])
def test_open_brewery_db_get_brewery(test_input, expected):
    r = requests.get('https://api.openbrewerydb.org/breweries/1')
    j = r.json()
    assert eval(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("r.status_code", 200), ("len(j) > 0", True)])
def test_open_brewery_db_search_breweries(test_input, expected):
    r = requests.get('https://api.openbrewerydb.org/breweries/search?query=dog')
    j = r.json()
    assert eval(test_input) == expected


def test_open_brewery_db_list_breweries_by_city():
    r = requests.get('https://api.openbrewerydb.org/breweries?by_city=san%20diego')
    j = r.json()
    assert len(j) > 0


def test_open_brewery_db_list_breweries_page():
    r = requests.get('https://api.openbrewerydb.org/breweries?page=1')
    j = r.json()
    assert len(j) > 0

