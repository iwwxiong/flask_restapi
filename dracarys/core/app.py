#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from flask import Flask, request
from werkzeug._compat import string_types, text_type
# dracarys import
from .responses import APIResponse
from .renders import JSONRender
from .exceptions import APIError


class APIFlask(Flask):
    """
    自定义APIFlask
    """
    response_class = APIResponse

    def make_response(self, rv):
        """

        """
        status_or_headers = headers = None
        if isinstance(rv, tuple):
            rv, status_or_headers, headers = rv + (None,) * (3 - len(rv))

        if rv is None:
            raise ValueError('View function did not return a response')

        if isinstance(status_or_headers, (dict, list)):
            headers, status_or_headers = status_or_headers, None

        if not isinstance(rv, self.response_class):
            # When we create a response object directly, we let the constructor
            # set the headers and status.  We do this because there can be
            # some extra logic involved when creating these objects with
            # specific values (like default content type selection).
            if isinstance(rv, (JSONRender, text_type, bytes, bytearray, list, dict)):
                rv = self.response_class(rv, headers=headers, status=status_or_headers)
                headers = status_or_headers = None
            else:
                rv = self.response_class.force_type(rv, request.environ)

        if status_or_headers is not None:
            if isinstance(status_or_headers, string_types):
                rv.status = status_or_headers
            else:
                rv.status_code = status_or_headers
        if headers:
            rv.headers.extend(headers)

        return rv

    def handle_api_exception(self, e):
        content = JSONRender(code=e.code, message=e.message)
        return self.response_class(content=content)

    def handle_user_exception(self, e):
        """
        自定义异常处理
        """
        exc_type, exc_value, tb = sys.exc_info()
        assert exc_value is e

        if isinstance(e, APIError):
            return self.handle_api_exception(e)

        # 暂不处理http异常，让系统抛出
        super(self.__class__, self).handle_user_exception(e)
