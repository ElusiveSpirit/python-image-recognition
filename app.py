import base64

from flask import Flask, jsonify, request, render_template
from io import BytesIO

from network import Network
from utils import load_image, get_networks, get_decision


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
networks = get_networks()


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

    value_list = [net.recognize(image_data) for net in networks]
    result = get_decision(value_list)
    image_data = Network.get_image_data(image_data)

    return jsonify({
        'digit': str(result['result']),
        'represented': image_data,
        'answers': [
            {
                'index': str(key),
                'count': str(value)
            }
            for key, value in result['answers'].items()
        ]
    })


if __name__ == '__main__':
    app.run()
