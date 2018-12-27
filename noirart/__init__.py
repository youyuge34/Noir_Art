# -*- coding: utf-8 -*-
import os

import click
from flask import Flask, render_template

from noirart.blueprints.auth import auth_bp
from noirart.blueprints.main import main_bp
from noirart.blueprints.user import user_bp
from noirart.extensions import bootstrap, db, mail, moment, login_manager, dropzone, csrf, avatars
from noirart.models import Role, User, Photo, Permission  # 导入之后db才能识别到，create的时候才会自动建表
from noirart.settings import config


# 工厂模式创建flask实例，flask会自动搜索名为create/make_app的方法
# 以后调用flask的current_app方法会返回app代理实例
def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('noirart')

    app.config.from_object(config[config_name])

    # 注册插件到app上
    register_extensions(app)
    # 注册蓝图
    register_blueprints(app)
    # 注册flask命令行
    register_commands(app)
    # 注册error handler
    register_errorhandlers(app)
    # 注册shell上下文
    register_shell_context(app)
    # 注册模板上下文
    register_template_context(app)

    return app


def register_extensions(app):
    login_manager.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    dropzone.init_app(app)
    csrf.init_app(app)
    avatars.init_app(app)


def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)


def register_shell_context(app):
    '''
    注册进shell上下文中，可直接调用db
    :param app:
    :return:
    '''
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, User=User, )


def register_template_context(app):
    '''
    返回一个dict，是固定唯一的常用数据，可在template中直接使用（e.g 分类列表）
    :param app:
    :return:
    '''
    pass


def register_errorhandlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(413)
    def request_entity_too_large(e):
        return render_template('errors/413.html'), 413

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        # 注意要之前import过继承db.model的model，这样db才能找到
        db.create_all()
        click.echo('Initialized database.')

    @app.cli.command()
    def init():
        """Initialize NoirArt. 运行程序前没forge咋办？用这个方法初始化角色权限数据库"""
        click.echo('Initializing the database...')
        db.create_all()

        click.echo('Initializing the roles and permissions...')
        Role.init_role()

        click.echo('Done.')

    @app.cli.command()
    @click.option('--user', default=10, help='Quantity of users, default is 10.')
    def forge(user):
        """Generate fake data."""

        from noirart.fakes import fake_admin, fake_user

        db.drop_all()
        db.create_all()
        click.echo('Initializing the roles and permissions...')
        Role.init_role()
        click.echo('Generating the administrator...')
        fake_admin()
        click.echo('Generating %d users...' % user)
        fake_user(user)
        click.echo('Done.')
