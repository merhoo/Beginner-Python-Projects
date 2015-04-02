'''
Created on Oct 18, 2011

@author: Meredith
'''
limit = int(input("Enter limit: "))
n = 1
if n > 0:
    while n <= limit:
        result = n* (n + 1) //2
        if n != 1:
            print(' ', end= '')
        print(result, end='')
        n += 1
    print()
print()    

