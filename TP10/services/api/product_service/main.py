from flask import Flask, request
from flask_cors import CORS
from datetime import datetime
import woody

app = Flask('product_service')
CORS(app)

@app.route('/api/products', methods=['GET'])
def add_product():
    product = request.args.get('product')
    woody.add_product(str(product))
    return str(product) or "none"

@app.route('/api/products/last', methods=['GET'])
def get_last_product():
    last_product = woody.get_last_product()
    return f'db: {datetime.now()} - {last_product}'

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return "not yet implemented"

if __name__ == "__main__":
    woody.launch_server(app, host='0.0.0.0', port=5000)