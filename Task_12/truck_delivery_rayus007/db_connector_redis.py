import socket
from truck_delivery_rayus007.util.configuration import Configuration

import redis
import json
from truck_delivery_rayus007.db_connector import DBConnector
from truck_delivery_rayus007.util.custom_exceptions import DataNotAvailableException


class DbConnectorRedis(DBConnector):
    def __init__(self):
        super(DbConnectorRedis, self).__init__()

    def get_connection(self):
        config = Configuration()
        try:
            if self.connection:
                return self.connection
            else:
                return redis.Redis(host=config.get_config_var("redis_host"),
                                   port=config.get_config_var("redis_port"),
                                   db=config.get_config_var("redis_db"))
        except (TimeoutError, ConnectionError, ConnectionAbortedError):
            raise TimeoutError("The DB is not available.")

    def save(self, id_save, object_to_save):
        encode_data = json.dumps(object_to_save)
        try:
            result_save = self.get_connection().set(id_save, encode_data)
        except DataNotAvailableException:
            raise ConnectionError("DB not available??")
        return result_save

    def get_by_id(self, id):
        result_get = self.get_connection().get(id)
        try:
            if result_get:
                return json.loads(result_get)
            else:
                return []
        except ConnectionError as conn_error:
            raise ConnectionError("What happened here!!!??")

    def get_all(self):
        list_objs = []
        try:
            list_ids = [id for id in self.get_connection().scan_iter(count=20)]
            if len(list_ids) > 0:
                list_objs = self.get_connection().mget(list_ids)
                list_objs = [json.loads(obj) for obj in list_objs]
            return list_objs
        except ConnectionError as conn_error:
            raise ConnectionError(f"Error given: {conn_error}")

    def delete_by_id(self, id):
        self.get_connection().delete(id)
        result_get = self.get_connection().get(id)
        if result_get:
            return result_get
        else:
            return []

    def get_by_pattern(self, pattern):
        pattern = f"{pattern}*"
        list_objs = []
        list_ids = [id for id
                    in self.get_connection().scan_iter(match=pattern, count=20)]
        if len(list_ids) > 0:
            list_objs = self.get_connection().mget(list_ids)
            list_objs = [json.loads(obj) for obj in list_objs]
        return list_objs
