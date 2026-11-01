# Super() =  Function used in a child class to call methods from a parent class (superclass)
#            Allos you to extend the functionality of the inherited methods 

class Shape:
    def __init__(self,color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled,radius):
        super().__init__(color, is_filled)      
        self.radius =radius

class Square(Shape):
    def __init__(self, color, is_filled,width):
        super().__init__(color, is_filled)   
        self.width = width


c1 = Circle(color="Red",is_filled=True,radius=56)
print(c1.color)
print(c1.is_filled)
print(c1.radius)

s1 = Square(color="Red",is_filled=True,width=156)
