"""
models.py

App Engine datastore models

"""

from google.appengine.ext import ndb
from werkzeug.security import generate_password_hash, check_password_hash


class User(ndb.Model):
    username = ndb.StringProperty()
    email = ndb.StringProperty()
    password = ndb.StringProperty()
    is_superuser = ndb.BooleanProperty(default=False)

    def is_admin_user(self):
        if self.is_superuser == True:
            return True

    def check_password(self, password):
        return check_password_hash(self.password, password)