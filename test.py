import pytest
from run import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    client = app.test_client()
    return client

@pytest.fixture
def route():
    return "http://127.0.0.1:5000"

def test_home(route, client):
    res = client.get(route + '/')
    assert res.status_code == 200

def test_about(route, client):
    res = client.get(route + '/about')
    assert res.status_code == 200

def test_register(route, client):
    res = client.get(route + '/register')
    assert res.status_code == 200

def test_register_email(route, client):
    res = client.post(route + '/register', data=dict(email='test@gmail.com', password='test'))
    assert b'That email is taken, Please choose a different one' in res.data

def test_register_username(route, client):
    res = client.post(route + '/register', data=dict(email='abc@gmail.com', username='測試人員', password='abc', confirm_password='abc'))
    assert b'That username is taken, Please choose a different one' in res.data

def test_login(route, client):
    res = client.post(route + '/login', data=dict(email='test@gmail.com', password='test'))
    assert res.status_code == 302
    assert 'http://127.0.0.1:5000/' == res.headers['Location']

def test_login_error(route, client):
    res = client.post(route + '/login', data=dict(email='test@gmail.com', password='iloveyou'))
    assert b'Login Unsuccessful. Please check email and password' in res.data

def test_post(route, client):
    assert client.get(route + '/post/1').status_code == 200

def test_post_error(route, client):
    assert client.get(route + '/post/999').status_code == 404

def test_newpost(route, client):
    client.post(route + '/login', data=dict(email='test@gmail.com', password='test'))
    assert client.get(route + '/post/new').status_code == 200

def test_newpost_post(route, client):
    client.post(route + '/login', data=dict(email='test@gmail.com', password='test'))

    res = client.post(route + '/post/new',data=dict(title='123456', content='123456', author='test'))
    assert res.status_code == 302
    assert 'http://127.0.0.1:5000/' == res.headers['Location']

def test_404(route, client):
    assert client.get(route + '/fksajmfksa').status_code == 404