'''
Created on Mar 5, 2012

@author: Meredith
'''
from datetime import date

class Person(object):
    def __init__(self, first_name, last_name, birthday):#constructor
        self.fisrt_name = first_name
        self.last_name = last_name
        self.birthday  = birthday
    def age(self):
        today = date.today()
        try:
            birthday= self.birthday.replace(year=today)
        except ValueError:
            birthday = self.birthday.replace(today.year,
                                             day = self.birthday.day - 1)
        if birthday > today:
            return today.year - self.birthday.year - 1
        else:
            return today.year - self.birthday.year
    def __str__(self):
        return self.first_name + " " + self.last_name

if __name__ == '__main__':
    obama  = Person("Barack", "Obama", date(1961, 8, 4))
    bush = Person("George", "Bush", date(1946, 7, 6))
    print(obama)