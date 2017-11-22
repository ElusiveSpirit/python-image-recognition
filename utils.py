import numpy as np

from PIL import Image


def prepare_img(img, size=(28, 28)):
    img = img.convert('L')
    img.thumbnail(size)
    return img


def get_img_data(img):
    img_data = img.getdata()
    img_data = np.array(list(map(lambda p: np.array([abs(p / 255 - 1)]), img_data)))
    return img_data


def load_image(image_file):
    img = prepare_img(image_file)
    img_data = get_img_data(img)
    return img_data


def load_image_from_file(image_file_name):
    img = Image.open(image_file_name)
    return load_image(img)
