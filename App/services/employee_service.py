from App.models.employee import Employee

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
