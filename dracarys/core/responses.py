#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'dracarysX'

from flask import Response
from werkzeug._compat import string_types, text_type
# dracarys import
from .renders import JSONRender
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
    可视图直接返回dict, list, string, response
    """
    default_mimetype = 'application/json'

    def __init__(self, content=None, *args, **kwargs):
        super(APIResponse, self).__init__(None, *args, **kwargs)
        if content is None:
            content = []
        if isinstance(content, (JSONRender, list, dict, text_type, string_types)):
            if isinstance(content, JSONRender):
                _content = content.render()
            elif isinstance(content, (dict, list, text_type, string_types)):
                _content = JSONRender(data=content).render()
            self.set_data(_content)

        # From `werkzeug.wrappers.BaseResponse`
        else:
            self.response = content
