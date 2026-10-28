# #class is blueprint for creating objects.

# class Student:
#     def __init__(self, name):
#         self.name = name
#         print("constructor call")

#     def welcome(self):
#         print("Welcome");   

#     def get_name(self):
#         return self.name

# class constructor and static method decorator example
# s = Student("Ganesh")
# print(s.name)
# s.welcome()
# s.get_name()

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks=marks

#     @staticmethod
#     def static_hello():
#         print("satatic method")    
#     def get_avg(self):
#         sum =0
#         for val in self.marks:
#             sum+=val
#         print(f"Hi {self.name} your avg marks = {round(sum/3)}")        

# s1 = Student("ganesh",[56,87,56])
# s1.get_avg()
# s1.static_hello()

class Car:
    def __init__(self):
        self.acc =False
        self.brk= False
        self.clutch = False


        https://www.youtube.com/watch?v=bAwmZVJeO5s