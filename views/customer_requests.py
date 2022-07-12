CUSTOMERS = [
    {
        "id": 1,
        "name": "Customer One"
    },
    {
        "id": 2,
        "name": "Customer Two",
    }
]


def get_all_customers():
    """Get all customers"""

    return CUSTOMERS


def get_single_customer(id):
    """Get customer by id"""
    # Variable to hold the found customer, if it exists
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer


def create_customer(customer):
    """Take the new dictionary representation sent by the client and append it to the CUSTOMERS list
    """
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer