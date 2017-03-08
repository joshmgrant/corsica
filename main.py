from flask import Flask, jsonify, abort, make_response, request
from numpy import random

app = Flask(__name__)

@app.errorhandler(400)
def invalid_value(error):
    return make_response(jsonify({'error': 'Invalid data request, check your parameters'}), 400)

@app.route('/corsica/help', methods=['GET'])
def get_help():
    h = {
        'title' : u'Corsica - Restful Random Samples',
        'description' : u'Return a list of samples of a desired distribution. Supported options are uniform(a,b), normal(mu, sigma) and exponential(l)'
    }
    return jsonify(h)

@app.route('/corsica/uniform/', methods=['GET'])
def get_uniform(a=0.0, b=1.0, n=10):
    a = request.args.get('a', a)
    b = request.args.get('b', b)
    samples = request.args.get('n', n)

    try:
        a = float(a)
        b = float(b)
        samples = int(samples)
    except ValueError:
        abort(400)

    if a > b:
        a, b = b, a
    elif abs(a - b) < 0.0001:
        abort(400)

    if samples <= 0:
        abort(400)
    
    r = random.uniform(a, b, samples).tolist()
    return jsonify({'samples' : r })

@app.route('/corsica/normal/', methods=['GET'])
def get_normal_dist(mu=0.0, sigma=1.0, n=10):
    m = request.args.get('mu', mu)
    s = request.args.get('sigma', sigma)
    samples = request.args.get('n', n)

    try:
        m = float(m)
        s = float(s)
        samples = int(samples)
    except ValueError:
        abort(400)

    if samples <= 0:
        abort(400)
    
    r = random.normal(m, s, samples).tolist()
    return jsonify({'samples' : r })

@app.route('/corsica/exponential/', methods=['GET'])
def get_exponential(l=1.0, n=10):
    m = request.args.get('lambda', l)
    samples = request.args.get('n', n)

    try:
        l = float(l)
        samples = int(samples)
    except ValueError:
        abort(400)

    if samples <= 0:
        abort(400)
    
    r = random.exponential(l, samples).tolist()
    return jsonify({'samples' : r })

if __name__ == '__main__':
    app.run(debug=True)