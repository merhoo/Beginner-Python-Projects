'''
Created on Oct 9, 2011

@author: Meredith
'''
import math

print("Let's create a list of three shapes...")
shape1 = input('Enter first shape: ')
shape2 = input('Enter second shape: ')
shape3 = input('Enter third shape: ')
shapes = [shape1, shape2, shape3]
print(shapes)
print()

print("Let's compute the circumference and area of a circle...")
radius = input('Enter radius: ')
circumference = float(radius) * 2 * math.pi
print('Circumference: ' + str(circumference))
area = (float(radius)**2 * math.pi)
print('Area: ' + str(area))