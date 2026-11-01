# Abstract class = A class that cannot be instantiated on its own; meant to be subclassed
#                  They can contain abstract methods, which are declare but have no implementation
#                  Abstract classes benefits:
#                  1. Trvents instantiation of class itself
#                  2. Requires children to use inherited abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
         pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You ride the car")

    def stop(self):
        print("You stop the car")    

car = Car()

car.go()
car.stop()
