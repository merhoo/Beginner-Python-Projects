'''
Created on Apr 25, 2012

@author: owner
'''
from abc import ABCMeta, abstractproperty

TYPE_TYPE = type(type)

class Pizza(metaclass=ABCMeta):
    @staticmethod
    def contains_ingredient(ingredient):
        return False

    @abstractproperty
    def price(self):
        return 0
    
class PizzaHamAndMushroom(Pizza):
    @staticmethod
    def contains_ingredient(ingredient):
        return ingredient in ("ham", "mushroom")
    
    @property
    def price(self):
        return 8.50
    
class PizzaHawaiin(Pizza):
    @staticmethod
    def contains_ingredient(ingredient):
        return ingredient in ("pineapple", "curry")
    
    @property
    def price(self):
        return 11.50
    
class PizzaFactory(object):
    @staticmethod
    def new_pizza(ingredient):
        pizza_classes = [j for (_, j) in globals().items() \
                         if isinstance(j, TYPE_TYPE) and issubclass(j, Pizza)]
        print(pizza_classes)
        for pizzaClass in pizza_classes:
            if pizzaClass.contains_ingredient(ingredient):
                return pizzaClass()
        raise ValueError("No pizza containing '%s'." % ingredient)     
if __name__ == "__main__":
    #pizza = Pizza()
    phm = PizzaHamAndMushroom()
    print("$%.2f" % phm.price)
    ph = PizzaHawaiin()
    print("$%.2f" % ph.price)
    print(globals())
    PizzaFactory.new_pizza("Pineapple")
    