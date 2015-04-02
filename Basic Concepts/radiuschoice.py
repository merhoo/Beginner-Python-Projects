'''
Created on Oct 9, 2011

@author: Meredith
'''
import math
radius = float(input('Enter radius: '))
circumference = (float(radius) * 2 * math.pi)
area = (float(radius) ** 2 * math.pi)
volume = (float(radius)**3 * 4/3 * math.pi)
choice = int(input('Choice (circumference = 1, area = 2, sphere = 3): '))
if choice == 1:
    print('Circumference: ' + str(circumference))
elif choice == 2:
    print('Area: ' + str(area))
elif choice == 3:
    print('Volume: ' + str(volume))
else:
    print('Error, enter valid answer')