employees = []


class Employee:
    def __init__(self, name, employee_id=1555):
        #employee = {"name": name, "employee_id": employee_id}
        self.name = name
        self.employee_id = employee_id
        employees.append(self)

    def __str__(self):
        return "Employee " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

Peter = Employee("Peter")
print(Peter)