#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask.json import JSONEncoder


class JSONRender(object):
    """
    >>> JSONRender(data=[]).render()
    {
        'status': {
            'code': 0,
            'message': '200 OK'
        },
        'data': []
    }
    """
    def __init__(self, code=0, message='200 OK', data=None):
        self.code = code
        self.message = message
        self.data = data or []

    def render(self):
        data = {
            'status': {
                'code': self.code,
                'message': self.message
            },
            'data': self.data
        }
        return json.dumps(data, cls=JSONEncoder, ensure_ascii=False)
