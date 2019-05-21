employees = []

def get_employees_titlecase():
    employees_titlecase = []
    for employee in employees:
        employees_titlecase.append(employee["name"].title())
    return employees_titlecase

#def print_employees_titlecase():#
    #employees_titlecase = []
    #employees_titlecase = employee.title()
    #print ("employees_titlecase")
#we simplify the above code by using the get function to
# pull the employee titlecase from the previously defined get funtcion

def print_employees_titlecase():
    employees_titlecase = get_employees_titlecase()
    print(employees_titlecase)

def add_employee(name, employee_id=1555):
    employee = {"name": name, "employee_id": employee_id}
    employees.append(employee)

def save_file(employee):
    
    try:
        f= open("employees.txt", "a")
        f.write(employee + "\n")
        f.close()
    except Exception:
        print("could not save file")

def read_file():
    try:
        f= open("employees.txt", "r")
        for employee in f.readlines():
            add_employee(employee)
        f.close()
    except Exception:
        print("Could not read file")


#def var_args (name, **kwargs):
   # print(name)
   # print(kwargs["sex"], kwargs["age"])

#employee_list = get_employees_titlecase()
#add_employee(name="Peter", employee_id=10001)
#var_args("Peter", sex="male", age="32", admin=True)

read_file()
print_employees_titlecase()
#Allow the employee to enter in their information
employee_name=input("Enter Employee Name: ")
employee_id=input("Enter Employee ID: ")

add_employee(employee_name, employee_id)
save_file(employee_name)
#print_employees_titlecase()