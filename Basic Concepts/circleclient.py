'''
Created on Nov 30, 2011

@author: Meredith
'''
import circle

def read_radius():
    radius = 0
    while True:
        radius = int(input('Enter radius: '))
        if radius >= 0:
            break
    return radius

def main():
    radius = read_radius()
    while radius != 0:
        area = circle.area(radius)
        circumference = circle.circumference(radius)
        print('Area is ' + str(area))
        print('Circumference is ' + str(circumference))
        radius = read_radius()

if __name__ == '__main__':
    main()