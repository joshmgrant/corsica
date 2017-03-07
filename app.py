from flask import Flask, jsonify, abort, make_response, request
from numpy import random

app = Flask(__name__)

@app.errorhandler(404)
def invalid_value(error):
    return make_response(jsonify({'error': 'Invalid data request'}), 404)

@app.route('/corsica/help', methods=['GET'])
def get_help():
    h = {
        'title' : u'Corsica - Restful Random Samples',
        'description' : u'Return a list of samples of a desired distribution. Supported options are uniform[a,b], normal(mean, sigma) and exponential(l)'
    }
    return jsonify(h)

@app.route('/corsica/samples/uniform/', methods=['GET'])
def get_uniform(a=0.0, b=1.0, n=1):
    a = request.args.get('a', a)
    b = request.args.get('b', b)
    samples = request.args.get('n', n)

    a = float(a)
    b = float(b)
    samples = int(samples)

    if a > b:
        a, b = b, a
    elif a == b:
        abort(404)

    if samples <= 0:
        abort(404)
    
    r = random.uniform(a, b, samples).tolist()
    return jsonify({'samples' : r })

@app.route('/corsica/samples/normal/', methods=['GET'])
def get_normal_dist(mean=0, sigma=1, n=1):
    m = request.args.get('mean', mean)
    s = request.args.get('sigma', sigma)
    samples = request.args.get('n', n)

    m = float(m)
    s = float(s)
    samples = int(samples)

    if samples <= 0:
        abort(404)
    
    r = random.normal(m, s, samples).tolist()
    return jsonify({'samples' : r })

if __name__ == '__main__':
    app.run(debug=True)