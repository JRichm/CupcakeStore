import csv
from flask import jsonify

def get_cart(file):
    print(f'{file}')
    # Retrieve the user's cart data from the CSV file
    with open('./csv/orderCupcakes.csv') as orderCupcakes:
        reader = csv.DictReader(orderCupcakes)
        rows = list(reader)
        print(rows)
        
    cart_data = rows
    print(cart_data)
    return cart_data
    
def add_custom(data):
    data = data['javascript_data']
    print(data)