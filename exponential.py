from flask import jsonify, abort, request
from numpy import random


def exponential_dist(lam=1.0, n=10):
    ld = request.args.get('lambda', lam)
    samples = request.args.get('n', n)

    try:
        ld = float(ld)
        samples = int(samples)
    except ValueError:
        abort(400)

    if samples <= 0:
        abort(400)

    if ld <= 0.0:
        abort(400)

    r = random.exponential(ld, samples).tolist()
    return jsonify({'samples': r})
