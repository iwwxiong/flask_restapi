#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = '10000573'

from flask.views import MethodView
from flask.globals import request


class APIMethodView(MethodView):
    """
    header: X-HTTP-Method-Override
    param: _method
    """

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
