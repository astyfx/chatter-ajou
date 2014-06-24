"""
decorators.py

Decorators for URL handlers

"""

from functools import wraps
from google.appengine.api import users
from flask import redirect, request, abort, g, url_for
from apps.models import User


def login_required(f):
    @wraps(f)
    def decorated_view(*args, **kwargs):
        if g.user is 'Guest':
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)

    return decorated_view


def admin_required(f):
    @wraps(f)
    def decorated_view(*args, **kwargs):
        user = User.query(User.username == g.user).get()

        if not user:
            return redirect(url_for('login', next=request.url))
        elif not user.is_admin_user():
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)

    return decorated_view