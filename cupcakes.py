import csv
from abc import ABC, abstractmethod
from pprint import pprint

class Cupcake(ABC):
    size = 'regular'
    def __init__(self, name, flavor, frosting, sprinkles, filling, price):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = sprinkles

    @abstractmethod
    def customize_cupcake(self, flavor, frosting, sprinkles, filling, price):
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = sprinkles
        self.filling = filling
        self.price = price

    @abstractmethod
    def calculate_price(self, quantity):
        return self.price * quantity


class Mini(Cupcake):
    size = 'mini'
    def __init__(self, name, flavor, frosting, sprinkles, filling, price):
        super().__init__(name, flavor, frosting, sprinkles, filling, price)

    def calculate_price(self, quantity):
        return super().calculate_price(quantity)

    def customize_cupcake(self, *args):
        return super().add_sprinkles(*args)

class Regular(Cupcake):
    size = 'regular'
    def __init__(self, name, flavor, frosting, sprinkles, filling, price):
        super().__init__(name, flavor, frosting, sprinkles, filling, price)

    def calculate_price(self, quantity):
        return super().calculate_price(quantity)

    def customize_cupcake(self, *args):
        return super().customize_cupcake(*args)
        
class Large(Cupcake):
    size = 'large'
    def __init__(self, name, flavor, frosting, sprinkles, filling, price):
        super().__init__(name, flavor, frosting, sprinkles, filling, price)

    def calculate_price(self, quantity):
        return super().calculate_price(quantity)

    def customize_cupcake(self, *args):
        return super().customize_cupcake(*args)

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

def write_new_csv(file, cupcakes):
    with open(file, 'w', newline = '\n') as csvfile:
        fieldnames = ['size', 'name', 'price', 'flavor', 'frosting', 'sprinkles', 'filling']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, 'filling'):
                writer.writerow({'size': cupcake.size,
                                 'name': cupcake.name,
                                 'price': cupcake.price,
                                 'flavor': cupcake.flavor,
                                 'frosting': cupcake.frosting,
                                 'filling': cupcake.filling,
                                 'sprinkles': cupcake.sprinkles})
            else:
                writer.writerow({'size': cupcake.size,
                                 'name': cupcake.name,
                                 'price': cupcake.price,
                                 'flavor': cupcake.flavor,
                                 'frosting': cupcake.frosting,
                                 'sprinkles': cupcake.sprinkles})

def add_cupcake(file, cupcake):
    with open(file, 'a', newline = '\n') as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr(cupcake, 'filling'):
            writer.writerow({'size': cupcake.size,
                             'name': cupcake.name,
                             'price': cupcake.price,
                             'flavor': cupcake.flavor,
                             'frosting': cupcake.frosting,
                             'filling': cupcake.filling,
                             'sprinkles': cupcake.sprinkles})
        else:
            writer.writerow({'size': cupcake.size,
                             'name': cupcake.name,
                             'price': cupcake.price,
                             'flavor': cupcake.flavor,
                             'frosting': cupcake.frosting,
                             'sprinkles': cupcake.sprinkles})
            
def get_cupcakes(file):
    with open(file) as storeCupcakes:
        reader = csv.DictReader(storeCupcakes)
        reader = list(reader)
        return reader

# write_new_csv("sample.csv", cupcake_list)
#read_csv("sample.csv")

myRegCupcake = Regular('someName', 'vanilla', 'chocolate', ['white'], 'chocolate', 2.00)

myRegCupcake.customize_cupcake('vanilla', 'chocolate', ['red'], 'chocolate', 2.00)
print(myRegCupcake.sprinkles)