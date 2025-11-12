from flask import Flask, render_template
import random as rnd

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    returns a short message on "localhost/"
    """
    return " hello World! "

names = ["John", "jane", "doe"]

@app.route('/rnd')
def get_random_number():
    rnd_name = rnd.choice(names)
    return f"hello {rnd_name}"

@app.route('/html')
def get_html_file():
    return render_template("index.html")
