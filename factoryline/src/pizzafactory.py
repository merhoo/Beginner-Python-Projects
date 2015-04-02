'''
Created on Apr 30, 2012

@author: Daniel Jin, David Zilburg, Jenna Ramos
'''
from abc import ABCMeta, abstractproperty
TYPE_TYPE = type(type)
import csv
import sys
ingredients_to_quantity = {}

def populate_dictionary(file_name):
    '''Opens filename and populates the ingredients_to_quanity dictionary
    with the values read from the file. Raises an IOError if the csv reader
    cannot open the file. If a line does not have the correct number 
    of fields, a ValueError is raised. The keys in ingredients_to_quanity are
    strings containing all the ingredients, each separated by a space, in 
    alphabetical order. The quantities of each type of pie are the values.
    
    Arguments:
    None

    Returns:
    None
    '''
    DB_File = file_name
    try:
        information = csv.reader(open(DB_File, newline = ''), \
                                       delimiter=',', quotechar='"')
    except IOError as error:
        print("I/O error (" + str(error.errno) + "): " + error.strerror + ".")
        sys.exit(1)
        
        
    try:
        for line in information:
            ingredient = line[1]
            quantity = line[0]
            ingredients_to_quantity[ingredient] = quantity
            
    except ValueError as error:
        print("Value Error(" + str(error.errno) + "): " + error.strerror + ".")
        sys.exit(1)
def tuple_to_str(tup):
    '''Takes a tuple of strings and returns them as a single string of series
    items. For example, the tuple ('ham', 'salami', 'cheese') would be
    returned as 'ham, salami, and cheese'.

    Arguments:
    tuple -- a tuple of strings

    Returns:
    A string of series items
    '''
    
    string = ''
    limit = len(tup) - 1
    count = 0
    for i in tup:
        if count != limit:
            string += i
            string += ', '
            count += 1
        elif count == 0 and count == limit:
            string += i
        else:
            string += 'and '
            string += i
    return string



class Pizza(metaclass=ABCMeta):
    @staticmethod
    def contains_ingredient(ingredient):
        return False
    @staticmethod
    def contains_all_ingredients(ingredients):
        return False
    @staticmethod
    def ingredients_as_string():
        return ""
    @abstractproperty
    def price(self):
        return 0

class PizzaHawaiian(Pizza):
    TOPPINGS = ("ham", "pineapple")
    @staticmethod
    def contains_ingredient(ingredient):
        return ingredient in PizzaHawaiian.TOPPINGS
    @staticmethod
    def contains_all_ingredients(ingredients):
        input_ingredients = ' '.join(sorted(ingredients.split()))
        ingredient_tuple = ("ham", "pineapple")
        ingredient_string = ' '.join(sorted(ingredient_tuple))
        if ingredient_string == input_ingredients:
            return True
        else:
            return False

    @staticmethod
    def ingredients_as_string():
        return tuple_to_str(PizzaHawaiian.TOPPINGS)
    
    @property
    def price(self):
        return 11.50
  
class PizzaPepperoni(Pizza):
    TOPPINGS = ("pepperoni",)
    @staticmethod
    def contains_ingredient(ingredient):
        return ingredient in PizzaPepperoni.TOPPINGS
    @staticmethod
    def contains_all_ingredients(ingredients):
        input_ingredients = ' '.join(sorted(ingredients.split()))
        ingredient_tuple = ("pepperoni",)
        ingredient_string = ' '.join(sorted(ingredient_tuple))
        if ingredient_string == input_ingredients:
            return True
        else:
            return False
    @staticmethod
    def ingredients_as_string():
        return tuple_to_str(PizzaPepperoni.TOPPINGS)
    
    @property
    def price(self):
        return 8.75


class PizzaVegetarian(Pizza):
    TOPPINGS = ("mushroom", "olive", "pepper")
    @staticmethod
    def contains_ingredient(ingredient):
        return ingredient in PizzaVegetarian.TOPPINGS
    @staticmethod
    def contains_all_ingredients(ingredients):
        input_ingredients = ' '.join(sorted(ingredients.split()))
        ingredient_tuple = ("mushroom", "olive", "pepper")
        ingredient_string = ' '.join(sorted(ingredient_tuple))
        if ingredient_string == input_ingredients:
            return True
        else:
            return False
    @staticmethod
    def ingredients_as_string():
        return tuple_to_str(PizzaVegetarian.TOPPINGS)
    
    @property
    def price(self):
        return 10.50

class PizzaFactory(object):
    @staticmethod
    def new_pizza(ingredients):
        """Creates a pizza out of the given ingredients string."""
        # Walk through all Pizza classes
        pizza_classes = [j for j in globals().values() if isinstance(j, TYPE_TYPE) and issubclass(j, Pizza)]
        for pizza_class in pizza_classes:
            if pizza_class.contains_all_ingredients(ingredients):
                pizza = pizza_class()
                return pizza
                # if research was unsuccessful, raise an error
        raise ValueError("No pizza containing '%s'." % ingredients)

def main():
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " <csv file>")
        sys.exit(1)
    populate_dictionary(sys.argv[1])
    total_price = 0.0
    for ingredients in ingredients_to_quantity.keys():
        currentprice = 0.0
        pizza_count = 0
        try:
            pizza = PizzaFactory.new_pizza(ingredients)
        except ValueError:
            print("No pizza containing '%s\' on menu. Skipping item..." % ingredients)
            continue
        for i in range(int(ingredients_to_quantity[ingredients])):
            currentprice += pizza.price
            pizza_count += 1
        total_price += currentprice
        ingredients_to_str = tuple_to_str(tuple(ingredients.split(" ")))
        if pizza_count == 1:
            print("Ordered 1 pizza at $%.2f with %s." % (pizza.price, ingredients_to_str))
        else:
            print("Ordered %d pizzas at $%.2f with %s." % (pizza_count, pizza.price, ingredients_to_str))
    print("-" * 20 + "\nTotal cost: $%.2f" % total_price)
    
if __name__ == "__main__":
    main()
    
        