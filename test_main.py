from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app)


def test_return_health_check():
    response = client.get("/health")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'status': 'Healthy'}


def test_query_search():
    requested_data = {
        "prompt": "rshar-Tnitldy.KnmfOXodpr(:6636-66460Ctakhm:HqdkZmc.",
        "k": 2
    }

    response = client.post('/query_search/', json= requested_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("Response")['ID'] == ["VectorID118", "VectorID117"]

