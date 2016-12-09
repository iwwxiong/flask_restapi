# -*-coding: utf-8 -*-

"""
config for tests.
"""

TESTING = True

from peewee import SqliteDatabase
DB_ENGINE = SqliteDatabase

# sqlite
DATABASE = {
    'database': 'dracarysX.db'
}