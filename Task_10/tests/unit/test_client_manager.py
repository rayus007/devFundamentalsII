import json
import pytest_mock
import pytest

from truck_delivery_rayus007.client_manager import ClientManager


@pytest.fixture
def client_manager(mocker):
    cli_manager = ClientManager()
    return cli_manager


def test_save_document_mock(mocker):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}
    cli_manager = ClientManager()
    mocker.patch("redis.Redis.set").return_value = True
    mocker.patch("redis.Redis.get").return_value = json.dumps(object_to_save)
    result_save = cli_manager.save_document(id_test, object_to_save)
    assert result_save is True


def test_get_by_id_mock(mocker):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}
    mocker.patch("redis.Redis.set").return_value = True
    mocker.patch("redis.Redis.get").return_value = json.dumps(id_test)
    cli_manager = ClientManager()
    cli_manager.save_document(id_test, object_to_save)
    result = cli_manager.get_document(object_to_save)
    assert str(result) == id_test


def test_get_all_mock(mocker):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}
    mocker.patch("redis.Redis.set").return_value = True
    mocker.patch("redis.Redis.get").return_value = json.dumps(id_test)
    cli_manager = ClientManager()
    cli_manager.save_document(id_test, object_to_save)
    result = cli_manager.get_all()
    assert result[0] == json.dumps(object_to_save)


def test_delete(mocker):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}
    mocker.patch("redis.Redis.set").return_value = True
    mocker.patch("redis.Redis.get").return_value = json.dumps(object_to_save)
    cli_manager = ClientManager()
    cli_manager.save_document(id_test, object_to_save)
    result = cli_manager.delete(id_test)
    assert result is None
