from truck_delivery_rayus007.util.constants import UID, CLIENT
from truck_delivery_rayus007.db_connector_redis import DbConnectorRedis
from truck_delivery_rayus007.content_manager import ContentManager
from truck_delivery_rayus007.util.custom_exceptions import CustomException


class ClientManager(ContentManager):
    """ Class representing a ClientManager """
    def __init__(self):
        super().__init__()
        self.connector = DbConnectorRedis()

    def save_document(self, key, document):
        try:
            result_save = self.connector.save(f"{UID}_{CLIENT}_{key}", document)
            return result_save
        except CustomException():
            print("This is a rayus exception")

    def get_document(self, key):
        result_json = self.connector.get_by_id(f"{UID}_{CLIENT}_{key}")
        return result_json

    def get_all(self):
        pattern = f"{UID}_{CLIENT}_"
        list_result = self.connector.get_by_pattern(pattern)
        return list_result

    def delete(self, key):
        return self.connector.delete_by_id(f"{UID}_{CLIENT}_{key}")

