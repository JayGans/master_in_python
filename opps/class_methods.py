class Student:
    count = 0
    total_gpa =0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"
    @classmethod
    def total_students(cls):
        return f"Total students are {cls.count}"

    @classmethod
    def get_total_gpa(cls):
        return f"Total GPA = {cls.total_gpa}"


s1 = Student("Amit", 8.0)
s2 = Student("Rakesh", 7.0)

print(s1.get_info())
print(Student.count)
print(Student.get_total_gpa())


