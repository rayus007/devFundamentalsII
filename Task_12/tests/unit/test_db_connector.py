import json
from truck_delivery_rayus007.db_connector_redis import DbConnectorRedis


def test_save_mock(mocker):
    mocker.patch("redis.Redis.set").return_value = True

    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    db_connector = DbConnectorRedis()
    result_save = db_connector.save(id_test, object_to_save)
    assert result_save is True


def test_get_by_id_mock(mocker):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}
    mocker.patch("redis.Redis.set").return_value = True
    mocker.patch("redis.Redis.get").return_value = json.dumps(object_to_save)

    db_connector = DbConnectorRedis()
    db_connector.save(id_test, object_to_save)

    result = db_connector.get_by_id(id_test)
    assert result == object_to_save


def test_get_all_mock(mocker):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    mocker.patch('redis.Redis.set').return_value = True
    mocker.patch('redis.Redis.get').return_value = json.dumps(object_to_save)

    db_connector = DbConnectorRedis()
    db_connector.save(id_test, object_to_save)

    result = db_connector.get_all()
    assert result[0] == object_to_save


def test_delete_object_mock(mocker):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    mocker.patch("redis.Redis.set").return_value = True
    mocker.patch("redis.Redis.get").return_value = json.dumps(object_to_save)

    db_connector = DbConnectorRedis()
    db_connector.save(id_test, object_to_save)

    result = db_connector.delete_by_id(id_test)
    assert result == object_to_save
