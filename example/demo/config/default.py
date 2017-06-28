# -*-coding: utf-8 -*-

"""
default config.
"""
from peewee import SqliteDatabase

DEBUG = True
SECRET_KEY = 'dracarysX'

# session
SESSION_COOKIE_NAME = 'sid'
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 7  # senven day

# Database

# sqlite

DB_ENGINE = SqliteDatabase

DATABASE = 'example.db'

# redis

# celery
