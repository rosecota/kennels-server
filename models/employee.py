class Employee():

    """
    A class used to represent an Employee

    ...

    Attributes
    ----------
    name : str
    address : str
    location_id : str
    """
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.

    def __init__(self, id, name, address, location_id):
        """
        Parameters
        ----------
        name : str
        address : str
        location_id : str
        """
        self.id = id
        self.name = name
        self.address = address
        self.location_id = location_id
