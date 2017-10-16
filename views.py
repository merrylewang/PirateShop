from flask import Flask, render_template,request,redirect,url_for
from .classes import Shop


app = Flask(__name__)

shop = Shop()   # Shop object from classes.py

@app.route("/", methods = ["POST","GET"])
def home():
    cost = 0
    cart = 0

    if request.method == "POST":
        # Accessing form and adding the movies into the cart
        d1 = request.form['EpisodeIV']
        d2 = request.form['EpisodeV']
        d3 = request.form['EpisodeVI']
        d4 = request.form['EpisodeIVBlu']
        d5 = request.form['EpisodeVBlu']
        d6 = request.form['EpisodeVIBlu']

        shop.add_many(shop.inventory[0], empty(d1))
        shop.add_many(shop.inventory[1], empty(d2))
        shop.add_many(shop.inventory[2], empty(d3))
        shop.add_many(shop.inventory[3], empty(d4))
        shop.add_many(shop.inventory[4], empty(d5))
        shop.add_many(shop.inventory[5], empty(d6))

        # Changing total price and number of items in shopping cart
        cost = shop.cost
        cart = shop.numberInCart
        return render_template(redirect(url_for("results")))

    return render_template("index.html", cost = cost, itemsInCart = cart)

# function to deal with an empty form and converting string to an int
def empty(s):
    if s == "":
        return 0
    else:
        return int(s)

@app.route("/", methods = ["POST","GET"])
def results():
    return render_template("results.html")





