import requests


Url = 'http://www.analog.com'


def get_responce():
    resp = requests.get(Url)
    if resp.ok:
        return resp
    else:
        return None

