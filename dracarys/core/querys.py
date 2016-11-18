#! /usr/bin/env python
# -*- coding: utf-8 -*-

from werkzeug.wrappers import Request, MultiDict, ImmutableMultiDict


class BaseQuery(object):
    """

    """
    def __init__(self, *args, **kwargs):
        pass


class PeeweeQuery(BaseQuery):
    """
    参数查询参考http://postgrest.com/api/reading/。
    """
    def __init__(self, model, params=None, *args, **kwargs):
        """
        
        :param model{peewee Model instance}:
        :param params{ImmutableMultiDict instance}:
        :return:
        """
        super(self.__class__, self).__init__(*args, **kwargs)
        self.model = model
        self.params = params
