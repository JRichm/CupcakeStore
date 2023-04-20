from flask import Flask, render_template, g
from cupcakes import get_cupcakes
app = Flask(__name__, static_url_path='/static')
import controller

@app.route("/")
def home():
    return render_template('index.html', cupcakes = get_cupcakes('./csv/storeCupcakes.csv'))

@app.route("/cupcakes")
def all_cupcakes():
    return render_template('cupcakes.html')

@app.route("/cupcake_individual")
def individual_cupcake():
    return render_template('individual-cupcake.html')

@app.route("/order")
def order():
    return render_template('order.html')

@app.route("/cart-data")
def cart_data():
    return controller.get_cart('./csv/orderCupcakes.csv')

if __name__ == "__main__":
    app.env = 'development'
    app.run(debug=True, port=8000, host='localhost')
