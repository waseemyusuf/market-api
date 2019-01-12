from flask import Flask, jsonify

app = Flask(__name__)

db = {
    'apple': 12.00,
    'mango': 01.99,
    'banana': 24.78
}

@app.route('/api/<string:product>', methods=['GET'])
def fruit_api(product):
    """Returns the price of a product"""

    # Check if product is valid
    if product not in db:
        return jsonify({'error': 'Invalid product'}), 422

    # Get the price
    price = db[product]
    return jsonify({
        'price': price
    })

if __name__ == '__main__':
    app.run()