'''
Created on Oct 25, 2011

@author: Meredith
'''

'''for loop for counting
range (startpoint, end point, update)\
startpoint = includes
endpoint = does not include
update = number by which to count

range(0, 10, 2)
output- 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

range(0,10,2)
output- 0, 2, 4, 6, 8

range(10, 0, -1)
10, 9, 8, 7, 6, 5, 4, 3, 2, 1

range(0, 10)
output 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

range(10)
0, 1, 2, 3, 4, 5, 6, 7, 8, 9

i,j,k are counting variables'''

s = 'Meredith Hoo'
for c in s:
    if c.isalnum():
        print(c)
    elif c.isalph():
        print(c)