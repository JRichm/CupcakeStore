from flask import jsonify
import csv
import cupcakes

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
    if data['size'] == 'mini':
        newCupcake = cupcakes.Mini(f'mini {data["name"]}', data['flavor'], data['frosting'], data['sprinkles'], data['filling'], float(data['price']) - 0.5)
    elif data['size'] == 'regular':
        newCupcake = cupcakes.Regular(f'regular {data["name"]}', data['flavor'], data['frosting'], data['sprinkles'], data['filling'], data['price'])
    elif data['size'] == 'large':
        newCupcake = cupcakes.Large(f'large {data["name"]}', data['flavor'], data['frosting'], data['sprinkles'], data['filling'], float(data['price']) + 1.00)
        
    file_path = './csv/orderCupcakes.csv'
    
    with open(file_path, 'r') as orderCupcakes:
        csv_reader = csv.DictReader(orderCupcakes)
        orders = list(csv_reader)
        
        
    #search for the new cupcake in the list of orders
    found = False
    for order in orders:
        if order['name'] == newCupcake.name and order['flavor'] == newCupcake.flavor and order['frosting'] == newCupcake.frosting and order['filling'] == newCupcake.filling:
            
            # if the cupcake is found, update the quantity
            order['quantity'] = str(int(order['quantity']) + 1)
            
            found = True
            break
    # if the cupcake is not found, add it ass a new row
    if not found:
        orders.append({'name': newCupcake.name,
                       'flavor': newCupcake.flavor,
                       'frosting': newCupcake.frosting,
                       'sprinkles': newCupcake.sprinkles,
                       'filling': newCupcake.filling,
                       'price': f'{newCupcake.price}',
                       'quantity': '1'})
        
    with open(file_path, 'w', newline='\n') as csv_file:
        fieldnames = ['name', 'flavor', 'frosting', 'sprinkles', 'filling', 'price', 'quantity']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(orders)
        