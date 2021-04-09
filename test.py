import pytest
import requests
from flask import url_for
from run import app
import json

@pytest.fixture
def test():
    x = 5
    return x

def test_index(test):
    y = 5
    assert test == y 

@pytest.fixture
def route():
    return "http://127.0.0.1:5000"

def test_home(route):
    res = requests.get(route + '/')
    assert res.status_code == 200

def test_about(route):
    res = requests.get(route + '/about')
    assert res.status_code == 200

def test_register(route):
    res = requests.get(route + '/register')
    assert res.status_code == 200

def test_login(route):
    url = route + '/login'
    data = dict(email='eyywqkgb@gmail.com', password='eyywqkgb')
    res = requests.post(url, data=data, allow_redirects=False)
    assert res.status_code == 200

def test_newpost(route):
    url = route + '/post/new'
    res = requests.get(url)
    assert res.status_code == 200

def test_404(route):
    url = route + '/fksajmfksa'
    res = requests.get(url)
    assert res.status_code == 404
