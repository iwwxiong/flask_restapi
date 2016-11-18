#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
# dracarys import
from .views import AuthorView

author_blueprint = Blueprint('book', __name__, url_prefix='/books')
author_view = AuthorView.as_view('authors')

author_blueprint.add_url_rule('', view_func=author_view, methods=['GET', ])
author_blueprint.add_url_rule('', view_func=author_view, methods=['POST', ])
author_blueprint.add_url_rule('/<book_id>', view_func=author_view, methods=['GET', ])
author_blueprint.add_url_rule('/<book_id>', view_func=author_view, methods=['PUT', 'DELETE', ])
