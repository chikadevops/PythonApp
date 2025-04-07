import sys
import os
import pytest

# Ensure the app.py file can be found and imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route_status_code(client):
    response = client.get('/')
    assert response.status_code == 200
