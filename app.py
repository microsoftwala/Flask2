from flask import Flask,render_template
import random
app = Flask(__name__)

# print(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route("/bad")
def bad():
    return'<h1 style="text-align:center">Hello world!</h1>' \
          '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width="200" style="border-radius:10px">'


@app.route("/user/<name>")
def greet(name):
    return f"Hi mr/mrs {name}, have a good day!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
