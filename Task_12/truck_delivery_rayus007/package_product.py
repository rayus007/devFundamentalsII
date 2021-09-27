class PackageProduct:
    """ Class representing a PackageProduct """
    def __init__(self, temperature_range, huminity_range, status):
        self.temperature_range = temperature_range
        self.huminity_range = huminity_range
        self.status = status

    def get_status(self):
        """
        get_status --> getting the PackageProduct status
        Return:
             result(dict)
        """
        return self.status
