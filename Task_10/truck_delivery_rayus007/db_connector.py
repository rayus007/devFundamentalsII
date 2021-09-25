from abc import ABCMeta, abstractmethod


class DBConnector(metaclass=ABCMeta):
    def __init__(self):
        self.connection = None

    @abstractmethod
    def get_connection(self):
        pass

    @abstractmethod
    def save(self, id_save, object_to_save):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def delete_by_id(self, id):
        pass

    @abstractmethod
    def get_by_pattern(self, pattern):
        pass
