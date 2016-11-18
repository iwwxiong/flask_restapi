#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask import request, g, current_app
# dracarys import
from dracarys.author.models import Author
from dracarys.core.responses import APIResponse


class AuthorView(MethodView):
    """

    """
    model = Author

    def get(self):
        print request.args
        return [1, 3, 4]

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
