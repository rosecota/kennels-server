EMPLOYEES = [
    {
        "id": 1,
        "name": "Employee One"
    },
    {
        "id": 2,
        "name": "Employee Two",
    }
]


def get_all_employees():
    """Get all employees
    """
    return EMPLOYEES


def get_single_employee(id):
    """Get employee by id
    """
    # Variable to hold the found employee, if it exists
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def create_employee(employee):
    """Take the new dictionary representation sent by the client and append it to the EMPLOYEES list
    """
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the employee dictionary
    employee["id"] = new_id

    # Add the employee dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee
