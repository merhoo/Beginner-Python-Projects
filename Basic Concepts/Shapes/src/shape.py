'''
Created on Apr 18, 2012

@author: Meredith
'''
from abc import ABCMeta, abstractproperty
#base class
class Shape(metaclass=ABCMeta):#super type, Objecct is the almighty god of types
    def __init__(self, x, y, name= "Shape"):#name is given a default value
        self.__name = name
        self.__x = x
        self.__y = y
        
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @x.setter
    def x(self, x):
        self.__x = x
        
    @y.setter
    def y(self, y):
        self.__y = y
    
    @abstractproperty
    def area(self):
        pass
    
    def __str__(self):
        return self.__name + " at (" + str(self.__x) +", " + str(self.__y) + ")"
    
if __name__ == "__main__":
    s = Shape()