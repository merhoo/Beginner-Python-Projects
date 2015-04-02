'''
Created on Apr 23, 2012

@author: Meredith
'''
from shape import Shape

class Circle(Shape):
    def __init__(self, x, y, radius, name):
        super().__init__(x, y, "Circle")
        self.__radius = radius
    
    @property    
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        self.__radius  = radius
        
    def __str__(self):
        return super().__str__() + " Radius: " + str(self.__radius)
    
if __name__=="__main__":
    cir = Circle(5, 5, 7, "Circle")
    print(cir)