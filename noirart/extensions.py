from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

# flask插件实例化
bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
moment = Moment()