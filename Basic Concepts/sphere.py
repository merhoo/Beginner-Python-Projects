'''
Created on Oct 9, 2011

@author: Meredith
'''
import math
print("Let's compute the circumference and area of a circle...")
radius = input('Enter radius: ')
circumference = float(radius) * 2 * math.pi
print('Circumference: ' + str(circumference))
area = (float(radius)**2 * math.pi)
print('Area: ' + str(area))