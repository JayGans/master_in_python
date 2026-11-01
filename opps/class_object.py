# object = A "bundle" of related attributes (variables) and methods(functions)
#       Ex. phone, cup, book
#       You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

class  Car:
    #class variable declare here
    def __init__(self, model, year, color, for_sale):    #dunder methode means double underscore methods
        #object variable declare here
        self.model = model
        self.year =  year
        self.color =color
        self.for_sale = for_sale


car1 = Car("mustang", 2024, "red", False)
print(car1.model)
        
