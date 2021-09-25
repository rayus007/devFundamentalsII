import redis
import json
from truck_delivery_rayus007.util.constants import UID
from truck_delivery_rayus007.content_manager import ContentManager


class VehicleManager(ContentManager):
    """ Class representing a VehicleManager """
    def __init__(self):
        super().__init__()
        self.cache = redis.Redis(host='localhost', port=6379, db=0)

    def save_document(self, document):
        self.cache.set(f"{UID}", json.dumps(document))

    def get_all(self):
        list_result = []
        for key in self.cache.scan_iter(f"{UID}_*"):
            list_result.append(json.loads(key))
        return list_result

    def get_document(self):
        result_json = self.cache.get(f"{UID}")
        return json.loads(result_json)

    def delete(self):
        self.cache.delete(f"{UID}")
