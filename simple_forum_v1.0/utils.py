import os
import secrets
from PIL import Image
from flask import current_app
from flask_login import current_user


def save_image(form_image):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_image.filename)
    image_filename = random_hex + f_ext
    image_path = os.path.join(current_app.root_path,
                              'static/prof_pics', image_filename)

    # ensures no overlapping
    while os.path.exists(image_path) is True:
        random_hex = secrets.token_hex(8)
        _, f_ext = os.path.splitext(form_image.filename)
        image_filename = random_hex + f_ext
        image_path = os.path.join(current_app.root_path,
                                  'static/prof_pics', image_filename)

    output_size = (125, 125)
    i = Image.open(form_image)
    i.thumbnail(output_size)
    i.save(image_path)

    # remove old profile picture (unless it is default)
    prev_image = os.path.join(current_app.root_path,
                              'static/prof_pics', current_user.prof_pic)
    if os.path.exists(prev_image) and current_user.prof_pic != 'default.png':
        os.remove(prev_image)

    return image_filename
