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

    def add_employee(self, imie, nazwisko, rola):
        new_id = len(self.employeesBase) + 1
        new_employee = Employee(new_id, imie, nazwisko, rola) 
        self.employeesBase.append(new_employee)
        

#TODO 
#  get_all() — zwraca wszystkich pracowników
#  get_by_id(id) — zwraca jednego pracownika
#  remove_employee(id) — usuwa pracownik

