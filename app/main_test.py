from fastapi.testclient import TestClient
from .main import *

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200

    response = client.get("/not-valid")
    assert response.status_code == 404


def test_import_csv():
    response = import_csv("bad path")
    expected = "File not found. There was an error with loading the Data!"
    assert response == expected

    response = import_csv("files/test.csv")
    assert response == {'Iron Man': {'movie': 'Iron Man',
                        'release_date': '2-May-08', 'release_order': '1'}}
