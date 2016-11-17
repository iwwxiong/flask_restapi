#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask import Blueprint
from flask import request, g, current_app
# dracarys import
from dracarys.author.models import Author

book_blueprint = Blueprint('book', __name__, url_prefix='/books')


class AuthorView(MethodView):
    """

    """
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
