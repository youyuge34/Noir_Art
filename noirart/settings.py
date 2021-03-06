import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class Operations:
    CONFIRM = 'confirm'
    RESET_PASSWORD = 'reset-password'
    CHANGE_EMAIL = 'change-email'


class BaseConfig:
    NOIR_ADMIN_EMAIL = os.getenv('NOIR_ADMIN', '1197993367@qq.com')
    NOIR_PHOTO_PER_PAGE = 12
    NOIR_COMMENT_PER_PAGE = 5
    NOIR_NOTIFICATION_PER_PAGE = 20
    NOIR_USER_PER_PAGE = 20
    NOIR_MANAGE_PHOTO_PER_PAGE = 20
    NOIR_MANAGE_USER_PER_PAGE = 30
    NOIR_MANAGE_TAG_PER_PAGE = 50
    NOIR_MANAGE_COMMENT_PER_PAGE = 30
    NOIR_SEARCH_RESULT_PER_PAGE = 20
    NOIR_MAIL_SUBJECT_PREFIX = '[Noir]'

    SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
    # flask内置服务器端验证
    MAX_CONTENT_LENGTH = 3 * 1024 * 1024  # file size exceed to 3 Mb will return a 413 error response.

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('Noir Admin', MAIL_USERNAME)

    NOIR_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    NOIR_PHOTO_SIZE = {'small': 400,
                         'medium': 800}
    NOIR_PHOTO_SUFFIX = {
        NOIR_PHOTO_SIZE['small']: '_s',  # thumbnail
        NOIR_PHOTO_SIZE['medium']: '_m',  # display
    }

    # dropzone参数
    DROPZONE_ALLOWED_FILE_TYPE = 'image'
    DROPZONE_MAX_FILE_SIZE = 3
    DROPZONE_MAX_FILES = 30
    DROPZONE_ENABLE_CSRF = True

    # 背景参数
    NOIR_THEMES = {'video': 'Video', 'photo': 'Photo'}

    # 默认头像参数
    AVATARS_SAVE_PATH = os.path.join(NOIR_UPLOAD_PATH, 'avatars')
    AVATARS_SIZE_TUPLE = (30, 100, 200)  # 三种尺寸的头像图片大小

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = \
        prefix + os.path.join(basedir, 'data-dev.db')
    REDIS_URL = "redis://localhost"


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'  # in-memory database


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',
                                        prefix + os.path.join(basedir, 'data.db'))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
