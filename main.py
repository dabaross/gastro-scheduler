from App.services.employee_service import EmployeeService

service = EmployeeService()
service.add_employee("Damian", "B", "barman")
service.get_all()
