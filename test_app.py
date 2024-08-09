# tests/test_app.py
import pytest
import io
import os
from flask import Flask
from werkzeug.datastructures import FileStorage
from app import app  

@pytest.fixture
def client():
    #Create a test client for the Flask app.
    with app.test_client() as client:
        yield client

def test_predict_page(client):
    #Test the predict page.
    response = client.get('/predict')
    assert response.status_code == 200
    assert b'Upload' in response.data 

def test_predict_invalid_file(client):
    #Test prediction with an invalid file.
    response = client.post('/predict', content_type='multipart/form-data', data={})
    assert response.status_code == 400
    assert 'error' in response.json  # Check that an error is returned

# def test_fail(client):
#     """This test is deliberately designed to fail"""
#     assert 1 + 1 == 3

@pytest.fixture(scope='module', autouse=True)
def cleanup():
    yield
    if os.path.exists('static/uploads/test_image.png'):
        os.remove('static/uploads/test_image.png')

