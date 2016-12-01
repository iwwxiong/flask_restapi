#! /usr/bin/env python
# -*- coding: utf-8 -*-


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
        return {
            'status': {
                'code': self.code,
                'message': self.message
            },
            'data': self.data
        }