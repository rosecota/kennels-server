class Customer():
    """
    A class used to represent a Customer

    ...

    Attributes
    ----------
    id: int
    name : str
    address : str
    email : str
      default = ""
    password : str
      default = ""
    """
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.

    def __init__(self, id, name, address, email="", password=""):
        """
        Parameters
        ----------
        id: int
        name : str
        address : str
        email : str
        password : str
        """
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password
