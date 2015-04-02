'''
Created on Apr 16, 2012

@author: Meredith
'''
class Account(object):
    num_account = 0#static variables
    def __init__(self, name, balance):#constructor
        self.__name = name
        self.__balance = balance
        Account.num_account += 1     
    def deposit(self, amount):#method
        self.__balance += amount
    def withdraw(self, amt):#method
        self.__balance = amt
    @property#mask the private variable
    def balance(self):
        return self.__balance
    @property
    def name(self):
        return self.__name
    def __str__(self):
        return self.__name + " $" + str(self.__balance)
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name is not valid")
        self.__name = name
    def __del__(self):#don't actually need this to delete things, used to  free up resources to maintain memory
        print("Deleting account for " + self.__name)
        self.__class__.num.accounts -= 1
        
if __name__ == "__main__":
    a = Account('Bill Borowski', 100)
    b = Account('Meredith Hoo', 200)
    print("Acount Name: " + str(a.name))
    print("Balance: $" + str(a.balance))
    a.name = "Brian Borowski"
    print(a)
    try:
        a.name = 5
    except TypeError as error:
        print(error)
    """lets say you have an account called a. 
    you can just do this instead of the del method
    a = Account("Bella", 90)
    del a"""
    print("Total accounts in bank: " + str(Account.num__accounts))
    print(a)
    print(b)
    del b
    print("Total accounts in bank: " + str(Account.num__accounts))