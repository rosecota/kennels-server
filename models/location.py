class Location():

    """
    A class used to represent a Location

    ...

    Attributes
    ----------
    name : str
    address : str
    """
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.

    def __init__(self, id, name, address):
        """
        Parameters
        ----------
        name : str
        address : str
        """
        self.id = id
        self.name = name
        self.address = address
