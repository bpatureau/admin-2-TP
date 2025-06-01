from flask import Flask, request
from flask_cors import CORS
from datetime import datetime
import woody
import redis

app = Flask('product_service')
CORS(app)

# Connexion Redis
redis_client = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

@app.route('/api/products', methods=['GET'])
def add_product():
    product = request.args.get('product')
    woody.add_product(str(product))

    # Invalide le cache (car la liste a changé)
    redis_client.delete('last_product')

    return str(product) or "none"

@app.route('/api/products/last', methods=['GET'])
def get_last_product():
    # Vérifie d'abord dans le cache
    cached_last = redis_client.get('last_product')
    if cached_last:
        return f'cache: {datetime.now()} - {cached_last}'

    # Sinon, calcule
    last_product = woody.get_last_product()

    # Stocke dans le cache pour 300s
    redis_client.setex('last_product', 300, last_product)

    return f'db: {datetime.now()} - {last_product}'

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return "not yet implemented"

if __name__ == "__main__":
    woody.launch_server(app, host='0.0.0.0', port=5000)
