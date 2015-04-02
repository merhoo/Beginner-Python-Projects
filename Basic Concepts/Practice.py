'''
Created on Apr 4, 2012

@author: Meredith
'''
class Person(object):
    def __init__(self, first_name, last_name, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__password = password
    def __str__(self):
        return self.__first_name + " " + self.__last_name + "'s password is " + self.__password
    @property
    def first_name(self):
        return self.__first_name
    @property
    def last_name(self):
        return self.__last_name
     
if __name__ == "__main__" :
    brian = Person("Brian", "Borowski", "apples")
