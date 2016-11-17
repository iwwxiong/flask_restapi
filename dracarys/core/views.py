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


