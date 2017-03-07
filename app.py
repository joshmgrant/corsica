from flask import Flask, jsonify, abort, make_response, request
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

@app.errorhandler(404)
def invalid_value(error):
    return make_response(jsonify({'error': 'Invalid sample value, must be positive integer'}), 404)

@app.route('/corsica/help', methods=['GET'])
def get_help():
    h = {
        'title' : u'Corsica - Restful Random Samples',
        'description' : u'Return a list of samples of a desired distribution. Supported options are uniform[0,1], binomial(n,p) and exponential(l)'
    }
    return jsonify(h)

@app.route('/corsica/samples/uniform/<int:samples>', methods=['GET'])
def get_uniform(samples):
    if samples <= 0:
        abort(404)
    
    r = random.uniform(0,1,samples).tolist()
    return jsonify({'samples' : r })



if __name__ == '__main__':
    app.run(debug=True)