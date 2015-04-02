'''
Created on Apr 17, 2012

@author: Meredith
'''
class Customer(object):
    def __init__(self, name):#encapsulate
        self.__name = name
    @property#lets you read private field name, but not change
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name is not a str")
        self.__name = name
    def __str__(self):
        return self.__name

if __name__ == "__main__":
    b = Customer('Brian Borowski')
    if isinstance(b, Customer):
        print("b is a customer")
    else:
        print("b is not a customer")
    print(b.name)
    print(b)
    print(b._Customer__name)#don't use
    b._Customer__name = "Bob"
    print(b)
