import pytest 
from apps.flask_app import app

@pytest.fixture
def client():
    # Set up the Flask test client
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    resp = client.get("/")
    assert resp.status_code == 200

def test_welcome_msg(client):
    resp = client.get("/deepak")
    assert resp.status_code == 200
    assert resp.data.decode('utf-8') == "Hello deepak, welcome"
    
def test_predict(client):
    test_data = {
        "km_driven": 45000,
        "mileage": 18,
        "age": 5,
        "fuel_type": "Petrol"
    }
    resp = client.post("/predict", json=test_data)
    assert resp.status_code == 200
    assert resp.json == { "predicted_price": 7.646241664886475 }