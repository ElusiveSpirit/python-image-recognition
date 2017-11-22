import base64

from flask import Flask, jsonify, request, render_template
from io import BytesIO

from network import Network
from utils import load_image


class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='(%',
        block_end_string='%)',
        variable_start_string='((',
        variable_end_string='))',
        comment_start_string='(#',
        comment_end_string='#)',
    ))


app = CustomFlask(__name__)
net = Network.load_from_file()


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/recognize/', methods=['POST'])
def recognize_file():
    data = request.get_json()
    if 'image' not in data:
        return jsonify({'msg': 'Image required'}), 400
    image = data['image'].split(',')[1]
    image_data = load_image(BytesIO(base64.b64decode(image)))
    value = net.recognize(image_data)
    layer = net.output_layer(image_data)
    image_data = net.get_image_data(image_data)

    return jsonify({
        'digit': int(value) if value else None,
        'represented': image_data,
        'layer': layer
    })


if __name__ == '__main__':
    app.run()
