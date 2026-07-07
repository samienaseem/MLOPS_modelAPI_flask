import pytest

from app import app

@pytest.fixture
def client():
    return app.test_client()


def test_ping(client):
    res=client.get("/ping")
    assert res.status_code == 200
    assert res.json ==  {"Message": "Hello from the server, yes i am active"} 


def test_predict(client):
    test_data={
        "Gender":"Male",
        "Married":"Unmarried",
        "Credit_History":"Unclear Debts",
        "ApplicantIncome":100000,
        "LoanAmount": 2000000
    }

    resp=client.post("/predict", json=test_data)
    assert resp.status_code == 200 
    assert resp.json=={"loan_application_status": "Rejected"}