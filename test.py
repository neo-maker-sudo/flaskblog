import pytest
import requests
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
    client = app.test_client()
    res = client.get(route + '/')
    assert res.status_code == 200

def test_about(route):
    client = app.test_client()
    res = client.get(route + '/about')
    assert res.status_code == 200

def test_register(route):
    client = app.test_client()
    res = client.get(route + '/register')
    assert res.status_code == 200

def test_login(route):
    client = app.test_client()
    res = client.get(route + '/login')
    assert res.status_code == 200

def test_404(route):
    client = app.test_client()
    res = client.get(route + '/fksajmfksa')
    assert res.status_code == 404
