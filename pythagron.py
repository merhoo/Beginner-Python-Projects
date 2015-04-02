'''
Created on Oct 28, 2011

@author: Meredith
'''
import time
total = 0 
print('--- Pythagorean Triple Generator ---\n')
max_value = float(input('Enter max value for c: '))
start = time.clock() # to be able to subtract the full time of the code minus the time it took the user to enter a max value
for a in range(1, int(max_value + 1)):
    for b in range (a, int(max_value + 1)): # It is limited down because it is only searching from a to max_value
        c = ((a*a + b*b)**.5)
        if c < max_value: 
            if c-b==1: # all c are 1 greater than b
                total+=1 # to print the number of Pythagorean triples
                print(str(total) + ':', a, b, int(c))
print('Searching Complete...')
print('Elapsed time:', time.clock() - start)