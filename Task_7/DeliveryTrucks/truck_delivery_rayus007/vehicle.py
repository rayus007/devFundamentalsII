from abc import ABCMeta, abstractmethod


class Vehicle(metaclass=ABCMeta):
    """Class to define basic information of a vehicle"""

    def __init__(self, typo, name):
        self.typo = typo
        self.name = name

    @abstractmethod
    def to_dict(self):
        """
        something --> This method changes to be implemented in children classes
        Arg:
        """
        pass
