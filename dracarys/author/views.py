#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask import request, g, current_app
# dracarys import
from dracarys.author.models import Author
from dracarys.core.querys import PeeweeObjectMixin
from dracarys.core.views import APIMethodView


class AuthorView(APIMethodView):
    """

    """
    model = Author
    paginate_by = 10

