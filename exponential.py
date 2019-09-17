from flask import jsonify, abort, make_response, request
from numpy import random

def exponential_dist(l=1.0, n=10):
    l = request.args.get('lambda', l)
    samples = request.args.get('n', n)

    try:
        l = float(l)
        samples = int(samples)
    except ValueError:
        abort(400)

    if samples <= 0:
        abort(400)
    
    if l <= 0.0:
        abort(400)

    r = random.exponential(l, samples).tolist()
    return jsonify({'samples' : r })
