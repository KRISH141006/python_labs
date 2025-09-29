import math
class Circle :
    
    def __init__(self,radius) :
        self.radius = radius

    def perimeter(self) :
        return 2*math.pi*self.radius
    
    def area(self) :
        return math.pi*self.radius**2
    
circle_A = Circle(5)
print("area of the circle is :",circle_A.area())
print("perimeter of the circle is :",circle_A.perimeter())