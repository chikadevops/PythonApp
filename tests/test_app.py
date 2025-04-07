import pytest
from app import app  # Import the Flask app
import re

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"http://ak-hdl.buzzfed.com/static" in response.data
