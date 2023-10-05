from flask import Flask, render_template, abort
import json

app = Flask(__name__)

# Sample product data in a JSON file
products = [
    {
        "name": "Fluent Python: Clear, Concise, and Effective Programming",
        "author": "Luciano Ramalho",
        "price": 39.95,
        "description": "Don't waste time bending Python to fit patterns you've learned in other languages. Python's simplicity lets you become productive quickly, but often this means you aren't using everything the language has to offer. With the updated edition of this hands-on guide, you'll learn how to write effective, modern Python 3 code by leveraging its best ideas.",
    },
    {
        "name": "Introducing Python: Modern Computing in Simple Packages",
        "author": "Bill Lubanovic",
        "price": 27.49,
        "description": "Easy to understand and fun to read, this updated edition of Introducing Python is ideal for beginning programmers as well as those new to the language. Author Bill Lubanovic takes you from the basics to more involved and varied topics, mixing tutorials with cookbook-style code recipes to explain concepts in Python 3. End-of-chapter exercises help you practice what you’ve learned.",
    },
]

# Home page
@app.route('/')
def home():
    return "Welcome to our website! Choose a page: <a href='/about'>About Us</a> | <a href='/contacts'>Contacts</a> | <a href='/products'>Products</a>"

# About Us page
@app.route('/about')
def about():
    return "About Us: We are a fantastic company with a great team!"

# Contacts page
@app.route('/contacts')
def contacts():
    return "Contact Us: Email us at iulian@bercu.com"

# Products listing page
@app.route('/products')
def product_listing():
    return render_template('product_listing.html', products=products)

# Product details page
@app.route('/product/<int:product_id>')
def product_details(product_id):
    if product_id >= 0 and product_id < len(products):
        return render_template('product_details.html', product=products[product_id])
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
