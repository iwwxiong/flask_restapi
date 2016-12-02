#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request, g, current_app
# dracarys import
from dracarys.core.views import APIMethodView
from .models import Book
from .forms import BookForm


class BookView(APIMethodView):
    """

    """
    model = Book
    paginate_by = 10
    context_object_name = 'items'
    pk_url_kwarg = 'book_id'
    form_class = BookForm
