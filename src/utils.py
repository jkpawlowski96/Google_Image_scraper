import string
import random
import os, shutil
import base64

TMP_LOCATION = os.environ.get('TMP_LOCATION', 'tmp')
TMP_LOCATION = os.path.realpath(TMP_LOCATION)

def create_tmp_dir():
    while True:
        dir_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        tmp_dir = os.path.join(TMP_LOCATION, dir_name)
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)
            return tmp_dir

def init_tmp_location():
    if os.path.exists(TMP_LOCATION):
        shutil.rmtree(TMP_LOCATION)
    os.makedirs(TMP_LOCATION)

def save_base64_images(images, directory):
    for i, image in enumerate(images):
        path = os.path.join(directory, str(i) + '.' + image.extension)
        with open(path, "wb") as f:
            f.write(base64.decodebytes(image.data))

def make_zip(directory):
    filename = os.path.basename(directory)
    zip_file = os.path.join(TMP_LOCATION, filename)
    shutil.make_archive(zip_file, 'zip', directory)
    return zip_file + '.zip'

def remove_directory(directory):
    shutil.rmtree(directory)