

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position =  position

    def display(self):
        return f"{self.name} = {self.position}"
    @staticmethod
    def is_valid_postion(position):
        valid_positions = ["Manager", "Cook"] 
        return position in valid_positions

emp1 = Employee("amit","Manager")  
emp2 = Employee("Rahul", "SDE")

print(emp1.display())

print(Employee.is_valid_postion(emp1.position))

print(emp2.display())

print(Employee.is_valid_postion(emp2.position))