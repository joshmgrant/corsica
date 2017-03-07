from flask import Flask, jsonify, abort, make_response
from numpy import random

app = Flask(__name__)

samples = [
    {
        'id': 1,
        'title': u'Uniform random variables',
        'description': u'Generate a list of uniform random samples.', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Binomial random variables',
        'description': u'Generate a list of binomial random samples', 
        'done': False
    }
]

@app.route('/corsica/help', methods=['GET'])
def get_help():
    h = {
        'title' : u'Corsica - Restful Random Samples',
        'description' : u'Return a list of samples of a desired distribution. Supported options are uniform[a,b], binomial(n,p) and exponential(l)'
    }
    return jsonify(h)

@app.route('/corsica/samples/<int:sample_id>', methods=['GET'])
def get_samples(sample_id):
    sample = [s for s in samples if s['id'] == sample_id]
    if len(sample) == 0:
        abort(404)
    return jsonify({'sample' : sample[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Invalid distribution name'}), 404)

if __name__ == '__main__':
    app.run(debug=True)