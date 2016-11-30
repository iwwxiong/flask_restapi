#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
from werkzeug.wrappers import ImmutableMultiDict


class QueryException(Exception):
    """

    """
    def __init__(self, message):
        super(QueryException, self).__init__()
        self.message = message


class BaseQuery(object):
    """

    """
    def __init__(self, *args, **kwargs):
        pass

    def get_query(self):
        raise NotImplementedError()


class PeeweeObjectMixin(object):
    """
    参数查询参考http://postgrest.com/api/reading/。
    """
    def query(self):
        query = self.pre_select()
        while len(self.joins) > 0:
            _obj = self.joins.pop()
            query = query.join(dest=_obj)
        where = self.where()
        if len(where) == 0:
            return query.order_by(*self.order())
        return query.where(*where).order_by(*self.order())

    def get_query(self):
        """

        :return:
        """
        if hasattr(self, '_query'):
            return self._query
        self._query = self.query()
        return self._query

    def count(self):
        """
        总数
        :return:
        """
        return self.get_query().count()

    def get_query_paginate(self):
        """
        分页查询
        :return:
        """
        return self.get_query()(*self.paginate())
