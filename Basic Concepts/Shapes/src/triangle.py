'''
Created on Apr 23, 2012

@author: Meredith
'''
from shape import Shape

class Triangle(Shape):
    def __init__(self, x, y, base, height, name):
        super().__init__(x, y, "Triangle")
        self.__base = base
        self.__height = height
    
    @property    
    def base(self):
        return self.__base
    
    @property
    def height(self):
        return self.__height
    
    @base.setter
    def base(self, base):
        self.__base = base
        
    @height.setter
    def height(self, height):
        self.__height = height

    def __str__(self):
        return super().__str__() + " Height: " + str(self.__height) + ", Base: "+ str(self.__base)
if __name__ == "__main__":
    tri = Triangle(10, 20, 3, 4, "Triangle")
    print(tri)