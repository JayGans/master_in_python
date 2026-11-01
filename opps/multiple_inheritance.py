# multiple inheritance = inherit from more than one parent class
#                         C(A,B)

class Animal:
    def __init__(self,name):
        self.name =name
        
    def eat(self):
        print(f"{self.name} is eating")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleein")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting") 

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

r1= Rabbit("Rabbit")
r1.flee()
r1.eat()

h1 = Hawk("Hawk")
h1.hunt()
h1.eat()

f1 = Fish("Fish")
f1.hunt()
f1.flee()
f1.eat()
