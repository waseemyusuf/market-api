import os
from models import *
from flask import Flask, jsonify, request

# Configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/api/products', methods=['GET'])
def fetch_all():

    isAvailable = request.args.get('available')
    if isAvailable:
        products = Product.query.filter(Product.inventory_count > 0).all()
    else:
        products = Product.query.all()

    response = {}

    for product in products:
        response['inventory_count'] = product.inventory_count
        response['price'] = product.price
        response['title'] = product.title
        response['id'] = product.id

    return jsonify(response)


@app.route('/api/products/<int:product_id>', methods=['GET'])
def fetch_one(product_id):
    # Check if product is valid
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Invalid product'}), 422

    # Get the price
    price = product.price
    return jsonify({
        'price': price
    })
