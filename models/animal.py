class Animal():

    """
    A class used to represent an Animal
    """
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.

    def __init__(self, id, name, breed, status, location_id, customer_id):
        """
        Parameters
        ----------
        name : str
            the name of the animal
        breed : str
            the breed of animal in the kennel
        status : str
            the kennel type status
        location_id : str
        customer_id : str
            the id of the customer who placed the animal in the kennel
        """
        self.id = id
        self.name = name
        self.breed = breed
        self.status = status
        self.location_id = location_id
        self.customer_id = customer_id
