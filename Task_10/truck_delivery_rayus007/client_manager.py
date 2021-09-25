import json
from truck_delivery_rayus007.util.constants import UID, CLIENT
from truck_delivery_rayus007.db_connector_redis import DbConnectorRedis
from truck_delivery_rayus007.content_manager import ContentManager


class ClientManager(ContentManager):
    """ Class representing a ClientManager """
    def __init__(self):
        super().__init__()
        self.connector = DbConnectorRedis()

    def save_document(self, key, document):
        result_save = self.connector.save(f"{UID}_{CLIENT}_{key}", json.dumps(document))
        return result_save

    def get_document(self, key):
        result_json = self.connector.get_by_id(f"{UID}_{CLIENT}_{key}")
        return json.loads(result_json)

    def get_all(self):
        patter = f"{UID}_{CLIENT}_"
        list_result = self.connector.get_by_pattern(patter)
        return list_result

    def delete(self, key):
        return self.connector.delete_by_id(f"{UID}_{CLIENT}_{key}")

