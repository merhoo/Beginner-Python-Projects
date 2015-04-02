'''
Created on Oct 18, 2011

@author: Meredith
'''

limit = int(input("Enter limit: "))  
a = 1
b = 1  
if limit >= 1:
    print(a, end='')
if limit >= 2:
    print('', b, end='')
n = 3
while n <= limit:
    c = a + b
    print('', c, end='') 
    a = b
    b = c
    n +=1
print()