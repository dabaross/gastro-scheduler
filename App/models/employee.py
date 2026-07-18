class Employee:
    def __init__(self, employee_id, name, surname, role, availability = None, hours_worked=None):
        self.employee_id = employee_id
        self.name = name
        self.surname = surname
        self.role = role
        
        if availability is None:
            availability = {}
        self.availability = availability
        
        if hours_worked is None:
            hours_worked = {}
        self.hours_worked = hours_worked
