#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'dracarysX'

from flask import Response
from werkzeug._compat import string_types, text_type


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
    可解释视图直接返回dict, list, string, response
    """
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
            self.set_data(content)
