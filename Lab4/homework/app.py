from flask import Flask, render_template
import os

app = Flask(__name__)

# Sample product data (you can load this from a JSON file)
products = [
    {
        "name": "Product 1",
        "author": "Author 1",
        "price": 19.99,
        "description": "Description for Product 1"
    },
    {
        "name": "Product 2",
        "author": "Author 2",
        "price": 29.99,
        "description": "Description for Product 2"
    }
]

# Define a directory to save simple page content
simple_page_content_directory = 'simple_page_content'

# Create the directory if it doesn't exist
if not os.path.exists(simple_page_content_directory):
    os.makedirs(simple_page_content_directory)


@app.route('/')
def home():
    content = "Welcome to the home page"
    # Save content to a file
    with open(os.path.join(simple_page_content_directory, 'home.txt'), 'w') as file:
        file.write(content)
    return content

@app.route('/about')
def about():
    content = "This is the about page"
    # Save content to a file
    with open(os.path.join(simple_page_content_directory, 'about.txt'), 'w') as file:
        file.write(content)
    return content

@app.route('/contacts')
def contacts():
    content = "Contact us at iulian@bercu.com"
    # Save content to a file
    with open(os.path.join(simple_page_content_directory, 'contacts.txt'), 'w') as file:
        file.write(content)
    return content


@app.route('/product/<int:product_id>')
def product(product_id):
    if 0 <= product_id < len(products):
        return render_template('product.html', product=products[product_id])
    else:
        return "Product not found", 404

@app.route('/product-listing')
def product_listing():
    return render_template('product_listing.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
