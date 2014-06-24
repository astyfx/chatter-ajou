import hashlib
import datetime
from apps import app


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


def generate_hash(key='', digits=8):
    return hashlib.sha1(key + str(datetime.datetime.now())).hexdigest()[:digits]