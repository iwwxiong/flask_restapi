#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'dracarysX'


class APIError(Exception):
    """

    """
    def __init__(self, code, message):
        self.code = code
        self.message = message


class APIError404(APIError):
    """

    """
    def __init__(self, message='Not Found'):
        super(APIError404, self).__init__(code=404, message=message)


class APIError403(APIError):
    """

    """
    def __init__(self, message='Forbidden'):
        super(APIError403, self).__init__(code=403, message=message)


class APIError500(APIError):
    """

    """
    def __init__(self, message='Forbidden'):
        super(APIError500, self).__init__(code=500, message=message)