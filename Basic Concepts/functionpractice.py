'''
Created on Dec 21, 2011

@author: Meredith
'''
#takes in the name
def mystery(name):
    print(name)# 1. not changed yet
    name = 'Brian'
    print(name)#2. prints

if __name__ == '__main__':
    name = 'Bryan'
    mystery(name)
    print(name)# 3
    

def confuse(i):
    print(12)
    i /= 3
    print(i)
    return i
if __name__ == '__main__':
    i = 12
    print(i)
    i = confuse(i)
    print(i)# i is a integer, integers are immutable

def eval_circle(degrees):
    if 0 <= degrees >= 89:
        return 'quarter'
    if 90 <= degrees <= 179:
        return 'half'