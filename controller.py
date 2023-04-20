import csv
from flask import jsonify

def get_cart(file):
    # Retrieve the user's cart data from the CSV file
    with open(file) as orderCupcakes:
        reader = csv.DictReader(orderCupcakes)
        rows = list(reader)
        
    cart_data = jsonify(rows)
    print(cart_data)
    return cart_data
    