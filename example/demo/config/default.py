# -*-coding: utf-8 -*-

"""
default config.
"""
from peewee import MySQLDatabase

DEBUG = True
SECRET_KEY = 'dracarysX'

# session
SESSION_COOKIE_NAME = 'sid'
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 7  # senven day

# Database

# mysql

DB_ENGINE = MySQLDatabase

DATABASE = {
    'database': 'dracarysX',
    'user': 'root',
    'passwd': '',
    'host': '127.0.0.1',
    'port': 3306,
}

# redis

# celery
