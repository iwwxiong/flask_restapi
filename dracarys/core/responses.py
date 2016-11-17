#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'dracarysX'

from flask.json import dumps
from flask import Response
from werkzeug._compat import string_types, text_type
# dracarys import
from .exceptions import APIError


class APIResponse(Response):
    """
    json format:
    {
        'status': {
            'code': 0,
            'message': 'success'
        },
        'data': []
    }
    """
    indent = 2
    separators = (', ', ': ')
    default_mimetype = 'application/json'

    def __init__(self, content=None, *args, **kwargs):
        super(APIResponse, self).__init__(response=None, *args, **kwargs)
        if isinstance(content, (list, dict, text_type, string_types)):
            if isinstance(content, (list, text_type, string_types)):
                content = {
                    'status': {
                        'code': 0,
                        'message': ''
                    },
                    'data': content
                }
            self.set_data((dumps(content, indent=self.indent, separators=self.separators), '\n'))
        raise APIError(code=500, message='syntax error')
