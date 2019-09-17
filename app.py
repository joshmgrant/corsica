from flask import Flask, jsonify, make_response, render_template
from normal import normal_dist
from uniform import uniform_dist
from exponential import exponential_dist


app = Flask(__name__)


@app.route('/')
@app.route('/corsica/')
def home_page():
    return render_template('home.html')


@app.errorhandler(400)
def invalid_value(error):
    error_msg = 'Invalid data request, check your parameters'
    return make_response(jsonify({'error': error_msg}), 400)


@app.route('/corsica/help', methods=['GET'])
def get_help():
    h = {
        'title': 'Corsica - Restful Random Samples',
        'description': 'Return a list of samples of a desired distribution. Supported options are uniform(a,b), normal(mu, sigma) and exponential(l)'
    }
    return jsonify(h)


@app.route('/corsica/uniform/', methods=['GET'])
def get_uniform(a=0.0, b=1.0, n=10):
    return uniform_dist(a, b, n)


@app.route('/corsica/normal/', methods=['GET'])
def get_normal_dist(mu=0.0, sigma=1.0, n=10):
    return normal_dist(mu, sigma, n)


@app.route('/corsica/exponential/', methods=['GET'])
def get_exponential(ld=1.0, n=10):
    return exponential_dist(ld, n)


if __name__ == '__main__':
    app.run(debug=True)
