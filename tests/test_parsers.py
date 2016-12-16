#! /usr/bin/env python
# -*- coding: utf-8 -*-

# dracarys import
from tests import BaseTestCase
from dracarys.core.parsers import QueryParser
from dracarys.book.models import Book, Author
from dracarys.core.app import APIFlask

environ = {
    'method': 'GET',
    'path': '/?select=id,name,author{id,name}&name=like.python&order=id.desc&limit=5&page=2'
}

app = APIFlask(__name__)
app.config['TESTING'] = True


class BookQP(QueryParser):
    """
    """
    model = Book
    paginate_by = 10


class QueryParserTests(BaseTestCase):
    """

    """
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