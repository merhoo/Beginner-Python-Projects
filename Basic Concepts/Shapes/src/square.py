'''
Created on Apr 20, 2012

@author: Meredith
'''
from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, x, y, length, name):
        super().__init__( x, y, length, length, "Square")
    
    @Rectangle.length.getter#can't make a property of a property in the super class
    def length(self):
        return self._Rectangle__length
    
    @length.setter
    def length(self, length):
        self._Rectangle__length = length
        self._Rectangle__width = length
#overriding = redefining a method that is already defined in a super class
#method signature ,ust be identical
    @Rectangle.width.getter
    def width(self):
        raise AttributeError("Square has no attribute 'width'.")
    
    @width.setter
    def width(self, width):
        raise AttributeError("Square has no attribute 'width'.")
        
    def __str__(self):
        return  super(Rectangle, self).__str__() + ",length = " + str(self.length)
    
    
    
if __name__ == "__main__":
    sqr = Square(10, 10, 10, 10)
    sqr.length = 50
    print(sqr)
    print("Area: " + sqr.area)
    