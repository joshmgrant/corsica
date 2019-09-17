from flask import jsonify, abort, request
from numpy import random


def normal_dist(mu=0.0, sigma=1.0, n=10):
    m = request.args.get('mu', mu)
    s = request.args.get('sigma', sigma)
    samples = request.args.get('n', n)

    try:
        m = float(m)
        s = float(s)
        samples = int(samples)
    except ValueError:
        abort(400)

    if s <= 0.0:
        abort(400)

    if samples <= 0:
        abort(400)

    r = random.normal(m, s, samples).tolist()
    return jsonify({'samples': r})
