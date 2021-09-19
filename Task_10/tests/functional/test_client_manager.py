import json
import pytest

from truck_delivery_rayus007.client_manager import ClientManager


@pytest.fixture
def client_manager(mocker):
    cli_manager = ClientManager()
    return cli_manager


def test_save_document(client_manager):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}
    result_save = client_manager.save_document(id_test, object_to_save)
    assert result_save is True


def test_get_by_id(client_manager):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}
    client_manager.save_document(id_test, object_to_save)
    result = client_manager.get_document(id_test)
    assert result == object_to_save


def test_get_all(client_manager):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}
    client_manager.save_document(id_test, object_to_save)
    result = client_manager.get_all()
    assert result[0] == json.dumps(object_to_save)


def test_delete(client_manager):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}
    client_manager.save_document(id_test, object_to_save)
    result = client_manager.delete(id_test)
    assert result is None
