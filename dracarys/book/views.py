#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request, g, current_app
# dracarys import
from dracarys.book.models import Book
from dracarys.core.views import APIMethodView


class BookView(APIMethodView):
    """

    """
    model = Book
    paginate_by = 10
    context_object_name = 'items'
    pk_url_kwarg = 'book_id'
