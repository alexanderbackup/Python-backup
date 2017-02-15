from functools import wraps
from django.shortcuts import redirect
from basicauth import views


def is_logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args[0].session.get('username', False):
            return func(*args, **kwargs)
        return redirect(views.login)
    return wrapper
