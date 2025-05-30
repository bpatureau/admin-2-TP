from flask import Flask, request
from flask_cors import CORS
from datetime import datetime
import woody

app = Flask('misc_service')
CORS(app)

@app.route('/api/misc/time', methods=['GET'])
def get_time():
    return f'misc: {datetime.now()}'

@app.route('/api/misc/heavy', methods=['GET'])
def get_heavy():
    name = request.args.get('name')
    r = woody.make_some_heavy_computation(name)
    return f'{datetime.now()}: {r}'

if __name__ == "__main__":
    woody.launch_server(app, host='0.0.0.0', port=5000)