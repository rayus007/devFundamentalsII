import json
import pytest

from api.views.main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_list_clients(client):
    receiver = client.get('/api/v1/clients')
    assert receiver.status_code == 200


def test_save_client(client):
    receiver = client.post('/api/v1/clients',
                           headers={"Content-Type": "application/json"},
                           json={"ci": 333333,
                                 "name": "Pepito3",
                                 "email": "pepito3.perez3@gmail.com",
                                 "cellphone": 3333333,
                                 "address": "cbba - Av. Heroinas",
                                 "contract_number": 333,
                                 "nit": 3333333333})
    assert receiver.status_code == 200


def test_get_client_by_id(client):
    receiver = client.get('/api/v1/clients/333333')
    assert receiver.status_code == 200


def test_delete_client_by_id(client):
    receiver = client.delete('/api/v1/clients/333333')
    assert receiver.status_code == 200
