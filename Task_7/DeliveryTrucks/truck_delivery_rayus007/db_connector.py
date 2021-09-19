from abc import ABCMeta, abstractmethod


class DBConnector(metaclass=ABCMeta):
    def __init__(self):
        self.connection = None

    @abstractmethod
    def get_connection(self):
        pass
