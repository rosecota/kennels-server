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
    return CUSTOMERS


def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
