import requests


def test1():
    url = 'http://localhost:5000/madlib'

    test = requests.get(url=url)

    assert test.status_code == 200