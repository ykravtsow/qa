import pytest
import requests


def test_url_status(url, status):
    r = requests.get(url)
    assert str(r.status_code) == status


