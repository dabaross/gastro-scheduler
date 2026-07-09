class Employee:
    def __init__(self, id, name, surname, role, availability=None, hours_worked=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.role = role
        self.availability = availability
        self.hours_worked = hours_worked



# TODO 
# 1. AvailabilityService: Szlify metody set_availability
#    - Dodać instrukcję `break` po znalezieniu pracownika (optymalizacja pętli).
#    - Dodać obsługę błędu (np. print), gdy pętla przejdzie całość i nie znajdzie pracownika (błędne ID).

# 2. AvailabilityService: Nowa metoda get_availability
#    - Napisać metodę def get_availability(self, employee_id):
#    - Metoda ma odszukać pracownika i zwrócić (lub wydrukować) jego aktualny słownik dyspozycji.

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
        # 1. Odszukaj pracownika w bazie (używając np. metody z employee_service)
        dyspo = {}
        dyspo[day] = time_range
        for employee in self.employee_service.employeesBase:
            if employee.id == employee_id:
                employee.availability.update(dyspo)
              # employee.availability.update({day: time_range})
                print("Dyspozycja dodana")


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

    def remove_employee(self, id):
        for employee in self.employeesBase:
            if employee.id == id:
                self.employeesBase.remove(employee)
                print(f"Usunieto pracownika z ID: {id}")
                break

main_employee_service = EmployeeService()