import os
from models import *
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/api/<int:product_id>', methods=['GET'])
def fruit_api(product_id):
    """Returns the price of a product"""

    # Check if product is valid
    product = Products.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Invalid product'}), 422

    # Get the price
    price = product.price
    return jsonify({
        'price': price
    })
