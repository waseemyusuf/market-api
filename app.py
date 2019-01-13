import os
from flask import Flask, jsonify, request
from models import *

# Configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/api/products', methods=['GET'])
def fetch_all():
    isAvailable = request.args.get('available')
    print(type(isAvailable))
    if isAvailable == 'true':
        products = Product.query.filter(Product.inventory_count > 0).all()
    else:
        products = Product.query.all()

    return jsonify({
        'products':[{
            'inventory_count': product.inventory_count,
            'price': product.price,
            'title': product.title,
            'id': product.id
        } for product in products]
    })


@app.route('/api/products/<int:product_id>', methods=['GET'])
def fetch_one(product_id):

    # Check if product is valid
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Invalid product id'}), 422

    return jsonify({
        'title': product.title,
        'price': product.price,
        'inventory_count': product.inventory_count,
        'id': product.id
    })

@app.route('/api/purchase/<int:product_id>', methods=['POST'])
def purchase(product_id):

    product = Product.query.get(product_id)

    # Check if product is valid
    if product is None:
        return jsonify({'error': 'Invalid product id'}), 422

    return product.purchase()