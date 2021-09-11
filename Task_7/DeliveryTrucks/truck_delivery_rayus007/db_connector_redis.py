import redis
from truck_delivery_rayus007.db_connector import DBConnector


class DbConnectorRedis(DBConnector):
    def __init__(self):
        super(DbConnectorRedis, self).__init__()

    def get_connection(self):
        if self.connection:
            return self.connection
        else:
            return redis.Redis(host='localhost', port=6379, db=0)


def test_connection():
    rayus = DbConnectorRedis()
    r = rayus.get_connection()
    print(r.set('test', 'OK!'))
    print(r.get('test'))
    print(r.acl_whoami())
    print(r.client_setname('Rayus007'))
    print(r.client_getname())
