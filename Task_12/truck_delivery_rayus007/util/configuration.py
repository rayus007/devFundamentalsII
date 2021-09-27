import yaml


class Configuration:

    def __init__(self, configuration=None):
        # read configuration.yml
        self.config = configuration if configuration else {}

    def get_config_var(self, key):
        config = {
            "redis_host": "localhost",
            "redis_port": 6379,
            "redis_db": 0
        }
        return config.get(key)

    def get_from_file(self, key):
        with open('truck_delivery_rayus007/configuration.yml') as my_file:
            my_vars = yaml.load(my_file)
            return my_vars.get(key)

    def get_from_env(self):
        pass
