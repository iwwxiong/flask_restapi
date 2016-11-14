# -*-coding: utf-8 -*-

"""
default config.
"""

DEBUG = True
SECRET_KEY = 'dracarysX'

# session
SESSION_COOKIE_NAME = 'sid'
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 7  # 7天

# Database

# sqlite
SQLITE_DATABASE = {
    'database': 'dracarysX.db'
}

# mysql
MYSQL_DATABASE = {
    'database': 'dracarysX',
    'user': 'root',
    'passwd': '',
    'host': '127.0.0.1',
    'port': 3306,
}

# redis

# celery
