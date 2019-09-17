from flask import jsonify, abort, request
from numpy import random


def uniform_dist(a=0.0, b=1.0, n=10):
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
    return jsonify({'samples': r})
