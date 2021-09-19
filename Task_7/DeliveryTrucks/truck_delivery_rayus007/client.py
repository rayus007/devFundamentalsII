from truck_delivery_rayus007.person import Person


class Client(Person):
    """ Class representing a Client """
    def __init__(self, ci, name, email, cellphone, address, contract_number, nit):
        super(Client, self).__init__(ci, name, email, cellphone, address)
        self.contract_number = contract_number
        self.nit = nit

    def to_dict(self):
        """
        to_dict --> getting the Client info
        Return:
             result(dict)
        """
        dict_init = self.__dict__
        return dict_init
