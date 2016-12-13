#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Request
# dracarys import
from tests import BaseTestCase
from dracarys.core.parsers import QueryParser
from dracarys.book.models import Book

request = Request(environ={
    'QUERY_STRING': 'select=id,name,author{id,name}&age=gt.254&order=id.desc&limit=5'
})


class QP(QueryParser):
    """
    """
    model = Book
    paginate_by = 10


class QueryParserTests(BaseTestCase):
    """

    """
    @classmethod
    def setUpClass(cls):
        BaseTestCase.setUpClass()
        cls.obj = QP()

    def test__args_split(self):
        print self.obj.args