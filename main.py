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


class ScheduleService:
    #ta klasa bedzie miala logike generowania grafiku i mozliwosc edycji oraz eksportu
    pass

# Availability wie: od kiedy pracownik może pracować.
# ScheduleService decyduje: którego pracownika wybrać.
#w bardziej sensownym modelu dyspozycyjność jest osobnym faktem biznesowym, który ma referencję do pracownika.
class Availability: #obiekt domenowy, pojedyncza deklaracaj dostępności pracownika
    def __init__(self, employee_id, date, start_time, end_time = None):
        self.employee_id = employee_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def can_close(self):
        if self.end_time is not None:
            return False
        if self.end_time is None:
            return True
#mówi nam CZYM JEST DYSPOZYCJA
# potrzebujemy tego obiektu aby móc go przypisac do kazdego dnia jako osobna dyspozycja danego pracownika na dany dzien
# dzieki temu dyspozycja przestaje byc surowymi danymi a staje sie bardziej funkcjonalnym obiektem
# który może powiedzieć np. praconik może zostać do zamknięcia. 
    
#mówi nam JAK DODAĆ / POBRAĆ / ZMIENIĆ dyspozycje
class AvailabilityService:
    def __init__(self, main_employee_service):
        self.employee_service = main_employee_service
        
    def set_availability(self, employee_id, date, start_time, end_time = None):
        worker = self.employee_service.get_by_id(employee_id)
        worker.availability[date] = Availability(employee_id, date, start_time, end_time)
        #pod konkretną datą zapisujemy konkretny obiekt Availability
        #ta funkcja może niczego nie zwracać bo jedynie zmienia stan atrybutu konkretnego obirktu Employee

    def get_availability(self, employee_id):
        worker = self.employee_service.get_by_id(employee_id)
        for day, time in worker.availability.items():
            print(f"{day} : {time}")
        return worker.availability

class ReservationService:
    #ta klasa bedzie zapiswyala do bazy danych rezerwacje 
    pass


class EmployeeService():
    def __init__(self):
        self.employeesBase = []
        self.id = 1

    def add_employee(self, name, surname, role):
        new_employee = Employee(self.id, name, surname, role) 
        self.employeesBase.append(new_employee)
        print(f"Added new employee with ID: {self.id}")
        self.id += 1
        return new_employee
        
    def get_all(self):
        for employee in self.employeesBase:
            print(f"ID: {employee.employee_id}, {employee.name}, {employee.surname}")

    def get_by_id(self, employee_id):
        for employee in self.employeesBase:
            if employee.employee_id == employee_id:
                print(f"ID: {employee.employee_id}, {employee.name}, {employee.surname}")
                return employee
        raise ValueError("Employee not found")
            
    def remove_employee(self, employee_id):
        for employee in self.employeesBase:
            if employee.employee_id == employee_id:
                self.employeesBase.remove(employee)
                print(f"Usunieto pracownika z ID: {employee_id}")
                break



main_employee_service = EmployeeService()
main_availability_service = AvailabilityService(main_employee_service)

main_employee_service.add_employee("damian", "b", "barman")
main_employee_service.add_employee("filip", "k", "kelner")

main_availability_service.set_availability(1, "Poniedzialek", "12")
main_availability_service.set_availability(2, "Wtorek", "15")

main_availability_service.get_availability(1)