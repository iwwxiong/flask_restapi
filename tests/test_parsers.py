#! /usr/bin/env python
# -*- coding: utf-8 -*-

# flask_restapi import
from peewee import *
from tests import DBTestCase
from flask_restapi.parsers import QueryParser
from flask_restapi.app import APIFlask
from flask_restapi.model import UUIDBaseModel
from flask_restapi.db import Database

environ = {
    'method': 'GET',
    'path': '/?select=id,name,author{id,name}&name=like.python&order=id.desc&limit=5&page=2'
}

app = APIFlask(__name__)
app.config['TESTING'] = True
db = Database(app, app.config.get('DB_ENGINE')(**app.config['DATABASE']))


class Author(UUIDBaseModel):
    """
    作者
    """
    id = PrimaryKeyField()
    name = CharField(max_length=50, unique=True)
    age = IntegerField(default=0)

    class Meta:
        db_table = 'Author'

    def __repr__(self):
        return u'<Author {}>'.format(self.name)


class Book(UUIDBaseModel):
    """
    书籍
    """
    id = PrimaryKeyField()
    name = CharField(max_length=255, unique=True)
    author = ForeignKeyField(Author, related_name='books')

    class Meta:
        db_table = 'Book'

    def __repr__(self):
        return u'<Book {}>'.format(self.name)


class BookQP(QueryParser):
    """
    """
    model = Book
    paginate_by = 10


class QueryParserTests(DBTestCase):
    """

    """
    @classmethod
    def tearDownClass(cls):
        db.close_db(None)
        super(QueryParserTests, cls).tearDownClass()

    def test__args_split(self):
        with app.test_request_context(**environ):
            qp = BookQP()
            self.assertEqual(qp._select_args, [[u'author.id', u'author.name'], u'id', u'name'])

    def test_select(self):
        with app.test_request_context(**environ):
            qp = BookQP()
            select = qp.select()
            self.assertIn(Book.id, select)
            self.assertIn(Book.name, select)
            self.assertIn(Author.id, select)
            self.assertIn(Author.name, select)

    def test_where(self):
        with app.test_request_context(**environ):
            qp = BookQP()
            where = qp.where()
            self.assertEqual([Book.name ** 'python'], where)

    def test_order(self):
        with app.test_request_context(**environ):
            qp = BookQP()
            order = qp.order()
            self.assertEqual(Book.id.desc(), order)

    def test_paginate(self):
        with app.test_request_context(**environ):
            qp = BookQP()
            paginate = qp.paginate()
            self.assertIn(2, paginate)
            self.assertIn(5, paginate)

    def test_pre_select(self):
        with app.test_request_context(**environ):
            qp = BookQP()
            query = qp.pre_select()
            self.assertEqual(
                Book.select(Book.id, Book.name, Author.id, Author.name).where(Book.name**'python').order_by(
                    Book.id.desc()), query)

