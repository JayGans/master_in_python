# Nested Class =  A class defined within another class
#                 class Outer:
#                      class Inner:

# Benefits: Allow you to logically group classes that are closely related
#           Encapsulated private details that arean't relevant outside of the outer class
#           keeps the namespace clean; reduces the possibility of naming conflict

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_emp = self.Employee(name,position)
        self.employees.append(new_emp)   

    def list_employee(self):
        return [emp.get_details() for emp in self.employees]   

cmp1 = Company("Amazon") 
cmp1.add_employee("Amit", "SDE")
cmp1.add_employee("Rajendra", "SDE II")

for emp in cmp1.list_employee():
    print(emp)
