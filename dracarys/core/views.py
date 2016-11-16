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
    method_list = ['put', 'delete', 'patch']

    def dispatch_request(self, *args, **kwargs):
        meth = getattr(self, request.method.lower(), None)
        # If the request method is HEAD and we don't have a handler for it
        # retry with GET.
        if meth is None and request.method == 'HEAD':
            meth = getattr(self, 'get', None)
        if meth == 'post':
            override = request.headers.get('HTTP-Method-Override', None)
            if override is not None and override in self.method_list:
                meth = getattr(self, override, None)
            _method = request.data.get('_method', None)
            if _method is not None and override in self.method_list:
                meth = getattr(self, _method, None)
        assert meth is not None, 'Unimplemented method %r' % request.method
        return meth(*args, **kwargs)

