from flask import Flask, request
from flask_cors import CORS
from datetime import datetime
import redis
import woody

app = Flask('misc_service')
CORS(app)

# Création du client Redis
redis_client = redis.Redis(host='redis', port=6379, db=0)

@app.route('/api/misc/time', methods=['GET'])
def get_time():
    return f'misc: {datetime.now()}'

@app.route('/api/misc/heavy', methods=['GET'])
def get_heavy():
    name = request.args.get('name', '')

    cache_key = f'heavy:{name}'
    cached_result = redis_client.get(cache_key)

    if cached_result:
        result = cached_result.decode('utf-8')
        return f'(from cache) {datetime.now()}: {result}'
    else:
        result = woody.make_some_heavy_computation(name)
        redis_client.setex(cache_key, 300, result)
        return f'(computed) {datetime.now()}: {result}'

if __name__ == "__main__":
    woody.launch_server(app, host='0.0.0.0', port=5000)
