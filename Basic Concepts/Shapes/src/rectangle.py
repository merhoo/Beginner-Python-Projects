'''
Created on Apr 20, 2012

@author: Meredith
'''
from shape import Shape

class Rectangle(Shape):#extends shape, this class is in Shape
    def __init__(self, x, y, length, width, name):
        super().__init__(x, y, "Rectangle")#calls constructor of the super class
        self.__length = length
        self.__width = width
   
    @property
    def length(self):
        return self.__length
    
    @property
    def width(self):
        return self.__width
    
    @length.setter
    def length(self, length):
        self.__length = length
    
    @width.setter
    def width(self, width):
        self.__width = width
    @property#uses dynamic binding
    def area(self):
        self.__length * self.__width

    def __str__(self):
        return super().__str__() + ", length = " + \
            str(self.__length) + ", width = " + str(self.__width)

if __name__ == "__main__":
    rect = Rectangle(10, 10, 20, 20, "Rectangle")
    rect.x = 30
    rect.y = 30
    print(rect)
    print("Rectangle at coordinates: (" + str(rect.x) + ", " + str(rect.y) + ")")
    print(isinstance(rect, Rectangle))
    print(isinstance(rect, Shape))
    print(isinstance(rect, object))
    print(isinstance(rect, str))
#instanciation- process of creating a instance of an object