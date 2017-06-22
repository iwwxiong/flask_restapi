# -*-coding: utf-8 -*-

from peewee import Proxy

db = Proxy()


class Database(object):
    def __init__(self, app=None, database=None):
        self.app = app
        self.database = database
        if self.app is not None:
            self.register_handlers()
        self.init_database()

    def init_database(self):
        db.initialize(self.database)

    def connect_db(self):
        # self.database.connect()
        self.database.get_conn()

    def close_db(self, exc):
        if not self.database.is_closed():
            self.database.close()

    def register_handlers(self):
        self.app.before_request(self.connect_db)
        self.app.teardown_request(self.close_db)
