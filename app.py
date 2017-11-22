from flask import Flask, jsonify, request, render_template
from io import BytesIO

from network import Network
from utils import load_image

app = Flask(__name__)
net = Network.load_from_file()


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/recognize/', methods=['POST'])
def recognize_file():
    if 'image' not in request.files:
        return jsonify({'msg': 'Image required'}), 400

    image = request.files['image']
    image_data = load_image(BytesIO(image.read()))
    value = net.recognize(image_data)

    return jsonify({'digit': int(value)})


if __name__ == '__main__':
    app.run()
