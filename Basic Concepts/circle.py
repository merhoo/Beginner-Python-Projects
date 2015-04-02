'''
Created on Nov 30, 2011

@author: Meredith
'''
import math

def area(radius):
    return math.pi * radius*radius
    
def circumference(radius):
    return math.pi *2 *radius

def print_name():
    print(__name__)

if __name__ == '__main__':
    print_name()
    print(area(5))
    print(circumference(5))