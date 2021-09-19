import redis
import json

from truck_delivery_rayus007.db_connector_redis import DbConnectorRedis
from truck_delivery_rayus007.util.constants import UID, DRIVER
from truck_delivery_rayus007.content_manager import ContentManager


class DriverManager(ContentManager):
    """ Class representing a DriverManager """
    def __init__(self):
        super().__init__()
        self.connector = DbConnectorRedis()

    def save_document(self, key, document):
        result_save = self.cache.set(f"{UID}_{DRIVER}_{key}", json.dumps(document))
        return result_save

    def get_document(self, key):
        result_json = self.connector.get_by_id(f"{UID}_{DRIVER}_{key}")
        return json.loads(result_json)

    def get_all(self):
        patter = f"{UID}_{DRIVER}_"
        list_result = self.connector.get_by_pattern(patter)
        return list_result

    def delete(self, key):
        return self.connector.delete_by_id(f"{UID}_{DRIVER}_{key}")
