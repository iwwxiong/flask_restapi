# -*-coding: utf-8 -*-

import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask import jsonify
from peewee import MySQLDatabase, SqliteDatabase
# dracarys import
from .core.app import APIFlask
from .middlewares.method_override import HTTPMethodOverrideMiddleware
from .core.exceptions import APIError
from .core.responses import APIResponse
from .core.db import Database


def create_app(testing=False):
    app = APIFlask(__name__, instance_relative_config=True)

    Bcrypt(app)

    # 加载默认配置
    app.config.from_object('config.default')

    # 加载环境变量
    environment = os.environ.get('ENVIRONMENT', 'development')

    # 载入相关配置
    app.config.from_object('config.{}'.format(environment))

    # 加载测试配置
    if testing:
        app.config.from_object('config.test')

    # 初始化数据
    Database(app, app.config.get('DB_ENGINE')(**app.config['DATABASE']))

    # 中间件
    app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)

    # 载入blueprint
    from .author import author_blueprint
    from .book import book_blueprint
    app.register_blueprint(author_blueprint)
    app.register_blueprint(book_blueprint)

    return app