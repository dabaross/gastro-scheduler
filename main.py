class Employee:
    def __init__(self, id, name, surname, role, availability = None, hours_worked=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.role = role
        
        if availability is None:
            availability = {}
        self.availability = availability
        
        if hours_worked is None:
            hours_worked = {}
        self.hours_worked = hours_worked


# TODO 
# 3. Testy "na sucho" (na samym dole pliku)
#    - Utworzyć obiekt EmployeeService i dodać 2-3 pracowników.
#    - Utworzyć obiekt AvailabilityService (wstrzyknąć mu EmployeeService).
#    - Wywołać set_availability i get_availability, żeby sprawdzić, czy dane poprawnie krążą.

# 4. ScheduleService (Nowy, główny moduł)
#    - Zaprojektować strukturę zapotrzebowania restauracji (np. ile osób na poranną/wieczorną zmianę).
#    - Przemyśleć szkielet metody generującej grafik, która będzie pobierać dyspozycje z AvailabilityService.


class ScheduleService:
    #ta klasa bedzie miala logike generowania grafiku i mozliwosc edycji oraz eksportu
    pass


class AvailabilityService:
    def __init__(self, main_employee_service):
        self.employee_service = main_employee_service
        
    def set_availability(self, employee_id, day, time_range):
        worker = self.employee_service.get_by_id(employee_id)
        worker.availability[day] = time_range

    def get_availability(self, emlpoyee_id):
        worker = self.employee_service.get_by_id(emlpoyee_id)
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
        
    def get_all(self):
        for employee in self.employeesBase:
            print(f"ID: {employee.id}, {employee.name}, {employee.surname}")

    def get_by_id(self, id):
        for employee in self.employeesBase:
            if employee.id == id:
                print(f"ID: {employee.id}, {employee.name}, {employee.surname}")
                return employee
            #TODO exception when Null
            
    def remove_employee(self, id):
        for employee in self.employeesBase:
            if employee.id == id:
                self.employeesBase.remove(employee)
                print(f"Usunieto pracownika z ID: {id}")
                break



main_employee_service = EmployeeService()
main_availability_service = AvailabilityService(main_employee_service)

main_employee_service.add_employee("damian", "b", "barman")
main_employee_service.add_employee("filip", "k", "kelner")

main_availability_service.set_availability(1, "Poniedzialek", "12")
main_availability_service.set_availability(2, "Wtorek", "15")

main_availability_service.get_availability(1)