import os
import operator
from collections import defaultdict

import numpy as np

from PIL import Image

from network import Network


def get_all_networks_files(basedir='./networks'):
    networks_files = []
    for dirname, _, filenames in os.walk(basedir):
        for filename in filenames:
            networks_files.append(os.path.join(dirname, filename))
    return networks_files


def get_networks():
    networks_files = get_all_networks_files()
    return [Network.load_from_file(f) for f in networks_files]


def get_decision(value_list):
    value_dict = defaultdict(int)
    for v in value_list:
        value_dict[v] += 1
    value_list = sorted(value_dict.items(), key=operator.itemgetter(1), reverse=True)
    result = value_list[0][0]
    if len(value_list) > 1:
        if value_list[0][0] is None and value_list[0][1] == value_list[1][1]:
            result = value_list[1][0]

    return {
        'result': result,
        'answers': value_dict
    }


def prepare_img(img, size=(28, 28)):
    img = img.convert('L')
    img.thumbnail(size)
    return img


def get_img_data(img):
    img_data = img.getdata()
    img_data = np.array(list(map(lambda p: np.array([abs(p / 255 - 1) if p != 0 else 0]), img_data)))
    return img_data


def load_image(image_file_name):
    img = Image.open(image_file_name)
    img = prepare_img(img)
    img_data = get_img_data(img)
    return img_data
