'''
Created on Oct 25, 2011

@author: Meredith
'''
# for loops are better for counting

#Exercise 2

'''sum = 0
for i in range(1, 11):
    sum += i
total = sum/10
print(total)


#Exercise 1

answer = 1 
base = int(input('Enter base: '))
exponent = int(input('Enter exponent: '))
if exponent == 0:
    print(str(base) + '^' +str(exponent) +' = 1' )
else:
    for i in range(exponent):
        answer *= base
    print(str(base) + '^' + str(exponent) + ' = ' + str(answer))'''

'''i =1 
ct = 1
for a in range(1,101):
    for b in range(a,101):
        i += 1
        for c in range(b,101):
            if a * b * c == 100:
                print(str(ct) + ':', a, b, c,)
                ct +=1
print(i)'''

p = 1
for i in range(2,7):
    p *= i
print(p)