import pytest
from truck_delivery_rayus007.db_connector_redis import DbConnectorRedis
import redis


def test_save():
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    db_connector = DbConnectorRedis()
    result_save = db_connector.save(id_test, object_to_save)
    assert result_save


def test_get_by_id():
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    db_connector = DbConnectorRedis()
    db_connector.save(id_test, object_to_save)

    result = db_connector.get_by_id(id_test)
    assert result == object_to_save


def test_get_all():
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    db_connector = DbConnectorRedis()
    db_connector.save(id_test, object_to_save)

    result = db_connector.get_all()
    assert result[0] == object_to_save


def test_delete_object():
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    db_connector = DbConnectorRedis()
    db_connector.save(id_test, object_to_save)

    result = db_connector.delete_by_id(id_test)
    assert result is None
