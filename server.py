from flask import Flask, render_template, g, request
from cupcakes import get_cupcakes
app = Flask(__name__, static_url_path='/static')
import controller

@app.route("/")
def home():
    return render_template('index.html', cupcakes = get_cupcakes('./csv/storeCupcakes.csv'))

@app.route("/cupcakes")
def all_cupcakes():
    return render_template('cupcakes.html')

@app.route("/order")
def show_current_order():
    return render_template('order.html')

@app.route("/orders")
def show_orders():
    return render_template('order.html')

@app.route("/customCupcake") # change route name to custom_Cupcake
def order():
    cartListData = controller.get_cart('./csv/orderCupcakes.csv')
    print('fart')
    print(cartListData)
    return render_template('customCupcake.html', cartListData=cartListData)

@app.route("/addCustom", methods=['POST'])
def add_custom():
    data = request.json
    if (data['javascript_data']['flavor'] == '' or
        data['javascript_data']['frosting'] == ''):
        return 'please select cake and flavor option'
    else:
        controller.add_custom(data)
        return 'success'
    

@app.route("/cart-data")
def cart_data():
    return controller.get_cart('./csv/orderCupcakes.csv')

if __name__ == "__main__":
    app.env = 'development'
    app.run(debug=True, port=8000, host='localhost')
