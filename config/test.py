# -*-coding: utf-8 -*-

"""
config for tests.
"""
from peewee import SqliteDatabase

TESTING = True

DB_ENGINE = SqliteDatabase

# sqlite
DATABASE = {
    'database': 'dracarysX.db'
}
