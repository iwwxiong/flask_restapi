#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request, g, current_app
# dracarys import
from dracarys.book.models import Book
from dracarys.core.querys import PeeweeObjectMixin
from dracarys.core.views import APIMethodView


class BookView(PeeweeObjectMixin, APIMethodView):
    """

    """
    model = Book
    paginate_by = 10

    def get(self):
        object_list = self.get_query()
        serializer = self.serializer_class(object_list=object_list, select_args=self._select_args)
        return serializer.data()

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

