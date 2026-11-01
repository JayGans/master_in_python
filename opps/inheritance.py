# Inheritance = Allow a class to inherit attributes and methods from another class 
#               Help with code reusability and extensibility
#               class child(parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Mouse(Animal):
    pass

dog = Dog("Scooby")
cat =Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name)
dog.eat()
dog.sleep()