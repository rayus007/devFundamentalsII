class ShippingRoute:
    """ Class representing a ShippingRoute """
    def __init__(self, start_place, end_place, truck, driver, client, package, status):
        self.start_place = start_place
        self.end_place = end_place
        self.truck = truck
        self.driver = driver
        self.client = client
        self.package = package
        self.status = status

    def get_current_location(self):
        """
        get_current_location --> getting the current location
        Return:
             result(string)
        """
        return self.truck.get_location()

    def get_current_status(self):
        """
        get_current_status --> getting the current status
        Return:
             result(string)
        """
        return self.package.get_status()

    def get_truck(self):
        """
        get_truck --> getting the truck details
        Return:
             result(truck)
        """
        return self.truck.get_truck()
