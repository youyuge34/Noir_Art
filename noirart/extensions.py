from flask_bootstrap import Bootstrap
from flask_login import LoginManager, AnonymousUserMixin
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_dropzone import Dropzone
from flask_wtf import CSRFProtect

dropzone = Dropzone()
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
moment = Moment()
csrf = CSRFProtect()


# 在每一个模板中都可以使用 current_user
# 因为session中只会存储登录用户的id(使用继承的UserMixin类重写了get_id方法），
# 所以为了让它返回对应的用户对象，我们还需要设置一个用户加载函数。
@login_manager.user_loader
def load_user(user_id):
    from noirart.models import User
    user = User.query.get(int(user_id))
    return user


'''
现在， 当我们调用current_user时， Flask-Login会调用上面↑这个函数
并返回对应的用户对象。 如果当前用户已经登录， 会返回User类实
例； 如果用户未登录， current_user默认会返回Flask-Login内置的
AnonymousUserMixin类对象， 它的is_authenticated和is_active属性会返
回False， 而is_anonymous属性则返回True。
'''

login_manager.login_view = 'auth.login'
# login_manager.login_message = 'Your custom message'
login_manager.login_message_category = 'warning'


class Guest(AnonymousUserMixin):
    '''
    为了让current_app都有can 和 is_admin 方法，重写访客登陆时的匿名类
    '''

    def can(self, permission_name):
        return False

    @property
    def is_admin(self):
        return False


login_manager.anonymous_user = Guest
