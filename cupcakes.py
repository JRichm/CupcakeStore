import csv
from abc import ABC, abstractmethod
from pprint import pprint

class Cupcake(ABC):
    size = 'regular'
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    @abstractmethod
    def add_sprinkles(self, *args):
        for sprinkle_type in args:
            self.sprinkles.append(sprinkle_type)

    @abstractmethod
    def calculate_price(self, quantity):
        return self.price * quantity


class Mini(Cupcake):
    size = 'mini'
    def __init__(self, name, price, flavor, frosting, filling):
        super().__init__(name, price, flavor, frosting, filling)
        self.sprinkles = []

    def calculate_price(self, quantity):
        return super().calculate_price(quantity)

    def add_sprinkles(self, *args):
        return super().add_sprinkles(*args)

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

cupcake1 = Mini("Stars and Stripes", 2.99, "Vanilla", "Vanilla", "Chocolate")
cupcake1.add_sprinkles("Red", "White", "Blue")
cupcake2 = Mini("Oreo", .99, "Chocolate", "Cookies and Cream", None)
cupcake2.add_sprinkles("Oreo pieces")
cupcake3 = Mini("Red Velvet", 3.99, "Red Velvet", "Cream Cheese", None)

cupcake_list = [
    cupcake1,
    cupcake2,
    cupcake3
]

write_new_csv("sample.csv", cupcake_list)
read_csv("sample.csv")
