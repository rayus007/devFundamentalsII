import json
import pytest

from truck_delivery_rayus007.client import Client
from truck_delivery_rayus007.client_manager import ClientManager


@pytest.fixture
def fixture_db_connector(mocker):
    client_to_save = Client(111111, "Pepito1", "pepito1.perez@gmail.com", 70700000, "Cbba - Av. Heroinas", 111,
                            1111111111).to_dict()
    mocker.patch("redis.Redis.set").return_value = True
    mocker.patch("redis.Redis.get").return_value = json.dumps(client_to_save)
    db_conn = ClientManager()
    return db_conn


def test_save_document_mock(fixture_db_connector):
    client_to_save = Client(111111, "Pepito1", "pepito1.perez@gmail.com", 70700000, "Cbba - Av. Heroinas", 111,
                            1111111111).to_dict()
    id_test = client_to_save.get("ci")
    result_save = fixture_db_connector.save_document(id_test, client_to_save)
    assert result_save is True


def test_get_by_id_mock(fixture_db_connector):
    client_to_save = Client(111111, "Pepito1", "pepito1.perez@gmail.com", 70700000, "Cbba - Av. Heroinas", 111,
                            1111111111).to_dict()
    id_test = client_to_save.get("ci")
    assert fixture_db_connector.save_document(id_test, client_to_save)
    result = fixture_db_connector.get_document(id_test)
    assert result == client_to_save


def test_get_all_mock(fixture_db_connector):
    client_to_save = Client(111111, "Pepito1", "pepito1.perez@gmail.com", 70700000, "Cbba - Av. Heroinas", 111,
                            1111111111).to_dict()
    id_test = client_to_save.get("ci")
    fixture_db_connector.save_document(id_test, client_to_save)
    result = fixture_db_connector.get_all()
    assert result[0] == client_to_save


def test_delete(fixture_db_connector, mocker):
    client_to_save = Client(111111, "Pepito1", "pepito1.perez@gmail.com", 70700000, "Cbba - Av. Heroinas", 111,
                            1111111111).to_dict()
    id_test = client_to_save.get("ci")
    fixture_db_connector.save_document(id_test, client_to_save)
    result = fixture_db_connector.delete(id_test)
    assert result is None
