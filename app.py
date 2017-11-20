import pickle

from flask import Flask, jsonify, request
from flask_redis import FlaskRedis

app = Flask(__name__)
redis_store = FlaskRedis(app)

TEACH_STATUS = 'teach_status'

##############################################################
#                       Utils
##############################################################


def redis_set(key, value):
    redis_store.set(key, pickle.dumps(value))


def redis_get(key):
    value = redis_store.get(key)
    if value:
        return pickle.loads(value)


def init():
    redis_set(TEACH_STATUS, {'status': None, 'percent': 0})


##############################################################
#                       Views
##############################################################

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/teach/', methods=['GET', 'POST'])
def teach_neural_net():
    if request.method == 'POST':
        # Start teaching
        pass
        return jsonify({'status': 'active', 'percent': 0}), 201
    status = redis_get(TEACH_STATUS)
    return jsonify(status)


@app.route('/recognize/', methods=['POST'])
def recognize_file():
    if 'image' not in request.files:
        return jsonify({'msg': 'Image required'}), 400
    image = request.files['image']
    print(image)
    return jsonify({'digit': 'Some recognized image'})


if __name__ == '__main__':
    init()
    app.run()
