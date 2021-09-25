import redis
import json
from truck_delivery_rayus007.db_connector import DBConnector


class DbConnectorRedis(DBConnector):
    def __init__(self):
        super(DbConnectorRedis, self).__init__()

    def get_connection(self):
        if self.connection:
            return self.connection
        else:
            return redis.Redis(host='localhost', port=6379, db=0)

    def save(self, id_save, object_to_save):
        encode_data = json.dumps(object_to_save)
        result_save = self.get_connection().set(id_save, encode_data)
        return result_save

    def get_by_id(self, id):
        result_get = self.get_connection().get(id)
        decode_data = json.loads(result_get)
        return decode_data

    def get_all(self):
        list_objs = []
        list_ids = [id for id in self.get_connection().scan_iter(count=20)]
        if len(list_ids) > 0:
            list_objs = self.get_connection().mget(list_ids)
            list_objs = [json.loads(obj) for obj in list_objs]
        return list_objs

    def delete_by_id(self, id):
        self.get_connection().delete(id)
        result_get = self.get_connection().get(id)
        return result_get

    def get_by_pattern(self, pattern):
        pattern = f"{pattern}*"
        list_objs = []
        list_ids = [id for id
                    in self.get_connection().scan_iter(match=pattern, count=20)]
        if len(list_ids) > 0:
            list_objs = self.get_connection().mget(list_ids)
            list_objs = [json.loads(obj) for obj in list_objs]
        return list_objs
