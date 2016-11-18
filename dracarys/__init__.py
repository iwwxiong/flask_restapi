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

app = APIFlask(__name__, instance_relative_config=True)

bcrypt = Bcrypt(app)

# 加载默认配置
app.config.from_object('config.default')

# 加载环境变量
environment = os.environ.get('ENVIRONMENT', 'development')

# 载入相关配置
app.config.from_object('config.{}'.format(environment))

# 初始化数据库（测试环境下使用sqlite数据库测试）
if environment == 'test':
    db = SqliteDatabase(**app.config['SQLITE_DATABASE'])
else:
    db = MySQLDatabase(**app.config['MYSQL_DATABASE'])

# 中间件
app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)

# 错误处理
# 注册方式一(装饰器模式)
# app.errorhandler(APIError)(lambda e: jsonify({
#     'status': {
#         'code': e.code,
#         'message': e.message
#     },
#     'data': []
# }))
# 注册方式二
app.register_error_handler(APIError, lambda e: jsonify({
    'status': {
        'code': e.code,
        'message': e.message
    },
    'data': []
}))

# 载入blueprint
from .author import author_blueprint
app.register_blueprint(author_blueprint)