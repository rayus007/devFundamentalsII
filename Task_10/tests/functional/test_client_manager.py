import json
import pytest

from truck_delivery_rayus007.client import Client
from truck_delivery_rayus007.client_manager import ClientManager


@pytest.fixture
def client_manager(mocker):
    cli_manager = ClientManager()
    return cli_manager


def test_save_document(client_manager):
    id_test = "111111"
    client_to_save = Client(111111, "Pepito1", "pepito1.perez@gmail.com", 70700000, "cbba - Av. Heroinas", 111,
                            1111111111).to_dict()
    result_save = client_manager.save_document(id_test, client_to_save)
    assert result_save is True


def test_get_by_id(client_manager):
    id_test = "111111"
    client_to_save = Client(111111, "Pepito1", "pepito1.perez@gmail.com", 70700000, "cbba - Av. Heroinas", 111,
                            1111111111).to_dict()
    client_manager.save_document(id_test, client_to_save)
    result = client_manager.get_document(id_test)
    assert result == client_to_save


def test_get_all(client_manager):
    id_test = "111111"
    client_to_save = Client(111111, "Pepito1", "pepito1.perez@gmail.com", 70700000, "cbba - Av. Heroinas", 111,
                            1111111111).to_dict()
    client_manager.save_document(id_test, client_to_save)
    result = client_manager.get_all()
    assert result[0] == json.dumps(client_to_save)


def test_delete(client_manager):
    id_test = "111111"
    client_to_save = Client(111111, "Pepito1", "pepito1.perez@gmail.com", 70700000, "cbba - Av. Heroinas", 111,
                            1111111111).to_dict()
    client_manager.save_document(id_test, client_to_save)
    result = client_manager.delete(id_test)
    assert result is None
