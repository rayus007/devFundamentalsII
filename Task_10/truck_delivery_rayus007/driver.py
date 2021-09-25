from truck_delivery_rayus007.person import Person


class Driver(Person):
    """ Class representing a Client """
    def __init__(self, ci, name, email, cellphone, address, license_number, license_country):
        super(Driver, self).__init__(ci, name, email, cellphone, address)
        self.license_number = license_number
        self.license_country = license_country

    def to_dict(self):
        """
        to_dict --> getting the Driver info
        Return:
             result(dict)
        """
        dict_init = self.__dict__
        return dict_init
