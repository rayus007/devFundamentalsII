import redis
from truck_delivery_rayus007.util.constants import UID, VEHICLE
from truck_delivery_rayus007.content_manager import ContentManager


class VehicleManager(ContentManager):
    """ Class representing a VehicleManager """
    def __init__(self):
        super().__init__()
        self.connector = redis.Redis(host='localhost', port=6379, db=0)

    def save_document(self, key, document):
        result_save = self.connector.save(f"{UID}_{VEHICLE}_{key}", document)
        return result_save

    def get_document(self, key):
        result_json = self.connector.get_by_id(f"{UID}_{VEHICLE}_{key}")
        return result_json

    def get_all(self):
        pattern = f"{UID}_{VEHICLE}_"
        list_result = self.connector.get_by_pattern(pattern)
        return list_result

    def delete(self, key):
        return self.connector.delete(f"{UID}_{VEHICLE}_{key}")
