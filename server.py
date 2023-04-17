from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello World!'

if __name__ == "__main__":
    app.env = 'development'
    app.run(debug=True, port=8000, host='localhost')
