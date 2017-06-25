#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'dracarysX'

from flask import Blueprint
# dracarys import
from flask_restapi.utils import register_api
from .views import BookView

book_blueprint = Blueprint('books', __name__, url_prefix='/books')
# register url
register_api(bp=book_blueprint, view=BookView, endpoint='books', pk='book_id')