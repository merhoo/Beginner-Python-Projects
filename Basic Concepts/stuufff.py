'''
Created on Apr 3, 2012, Her Birthday

@author: Meredith
'''

class Computer(object):
    def __init__(self, processor, manufacturer, op_sys, year):
        #initialize the fields in this constructor
        self.processor = processor
        self.manufacturer = manufacturer
        self.op_sys = op_sys
        self.year = year

class Processor(object):
    AMD = 0
    INTEL = 1
    def __init__(self, brand, speed, num_cores):
        self.brand = brand
        self.speed= speed
        self.num_cores = num_cores
        if brand == 0:
            self.brand_name = "AMD"
        else:
            self.brand_name = "INTEL"
    def ___str___(self):
        return 'Brand :' + self.brand_name + self.speed + "" + "m"
    
if __name__ == "__main__":
    processor = Processor(Processor.AMD, 3.0, 4)
    

        
