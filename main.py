class Employee:
    def __init__(self, id, name, surname, role, availability, hours_worked):
        self.name = name
        self.surname = surname
        self.role = role
        self.availability = availability
        self.hours_worked = hours_worked

class ScheduleService:
    #ta klasa bedzie miala logike generowania grafiku i mozliwosc edycji oraz eksportu
    pass

class AvailabilityService:
    #ta klasa bedzie miala logike podawania dyspo
    pass

class ReservationService:
    #ta klasa bedzie zapiswyala do bazy danych rezerwacje 
    pass

class EmployeeService():
    def __init__(self):
        self.employeesBase = []

    def add_employee(self, name, surname, role):
        new_id = len(self.employeesBase) + 1
        new_employee = Employee(new_id, name, surname, role) 
        self.employeesBase.append(new_employee)
        
    def get_all(self):
        for employee in self.employeesBase:
            print(f"ID {employee.id}, {employee.name}, {employee.surname}")

    def get_by_id(self, id):
        for employee in self.employeesBase:
            if employee.id == id:
                print(f"ID: {employee.id}, {employee.name}, {employee.surname}")

    def remove_employee(self, id):
        for employee in self.employeesBase:
            if employee.id == id:
                self.employeesBase.remove(employee)
                break



