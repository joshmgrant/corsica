from flask import Flask
from numpy import random

app = Flask(__name__)

@app.route('/')
def index():
    r = random.uniform(0,1)
    return str(r)

if __name__ == '__main__':
    app.run(debug=True)