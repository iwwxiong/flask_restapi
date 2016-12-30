#! /usr/bin/env python
# -*- coding: utf-8 -*-

# flask_restapi import
from flask_restapi.views import APIMethodView
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
