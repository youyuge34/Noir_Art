from functools import wraps

from flask import Markup, flash, url_for, redirect, abort
from flask_login import current_user


# 带参数的装饰器定义函数
def permission_required(permission_name):
    def decorator(func):
        @wraps(func)  # 为了wrapper.__name__ = func.__name__，否则函数name变为wrapper
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission_name):
                abort(403)
            return func(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(func):
    return permission_required('ADMINISTER')(func)
