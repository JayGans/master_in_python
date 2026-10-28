class Employee:
    count =0

    def __init__(self,name,salary,designation):
        self.name=name
        self.salary =salary
        self.designation = designation
        Employee.count+=1

    def EmployeProfile(self):
        print("Name: ", self.name)
        print("Salary: ",self.salary)
        print("Designation: ", self.designation)



e = Employee("Ganesh","23454","SDE -II")
print(e.count)  
e1= Employee("Amit","7654","QA")
print(e.count)  

e.EmployeProfile()
e.count=100 
del Employee.count
print(Employee.count) 
     