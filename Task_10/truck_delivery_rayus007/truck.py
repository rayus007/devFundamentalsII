from truck_delivery_rayus007.vehicle import Vehicle


class Truck(Vehicle):
    """ Class representing a Truck """
    def __init__(self, typo, name, license_plate, model, brand_manufactor):
        super(Truck, self).__init__(typo, name)
        self.license_plate = license_plate
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

