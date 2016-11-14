# -*-coding: utf-8 -*-

import os
from flask import Flask
from flask_bcrypt import Bcrypt
from peewee import MySQLDatabase, SqliteDatabase


app = Flask(__name__, instance_relative_config=True)
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
