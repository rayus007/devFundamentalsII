from truck_delivery_rayus007.vehicle import Vehicle


class Truck(Vehicle):
    """ Class representing a Truck """
    def __init__(self, license_plate, typo, model, brand_manufactor):
        self.license_plate = license_plate
        self.typo = typo
        self.model = model
        self.brand_manufactor = brand_manufactor

    def to_dict(self):
        """
        to_dict --> getting the Truck info
        Return:
             result(dict)
        """
        dict_init = self.__dict__
        return dict_init

    def get_truck(self):
        return self

