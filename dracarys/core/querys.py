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


class PeeweeQueryMixin(object):
    """
    参数查询参考http://postgrest.com/api/reading/。
    """
    model = None
    paginate_by = None
    where_exclude = ['select', 'order', 'page', 'limit']
    page_param = 'page'

    def __init__(self):
        from flask import request
        from .conditions import mappings
        self.args = request.args
        self.mappings = mappings
        self.joins = set()

    def _handle_select(self):
        """
        >>> ImmutableMultiDict([('select', 'id, name, age, author{id, name}')])
        Book.select(Book.id, Book.name, Book.age, Author.id, Author.name)
        """
        select = []
        params = self.args['select'].split(',')
        r = re.compile(r'^(?P<key>\w+){(?P<value>.+)}$')

        def _handel(obj, _params):
            for param in _params:
                if r.search(param):
                    key, value = r.search(param).groups()
                    _obj = obj._meta.fields[key].rel_model
                    self.joins.add(_obj)
                    if value == '*':
                        select.append(_obj)
                    else:
                        _handel(_obj, value.split(','))
                else:
                    select.append(obj._meta.fields[param])

        _handel(self.model, params)
        return select

    def select(self):
        if 'select' in self.args:
            return self.model.select()
        select = self._handle_select()
        return self.model.select(*select)

    def where(self):
        """
        >>> ImmutableMultiDict([('name', 'dracarysX'), ('age', 'lt.30')])
        where(Book.name == 'dracarysX', Book.age > 30)
        """
        params = {key: value for key, value in self.args.items() if key not in self.where_exclude}
        where = []
        for k, v in params.items():
            if k in self._meta.fields:
                value = v.split('.')
                if len(value) == 0:
                    where.append(self.mappings['eq'](self.model, k, v).to_peewee())
                else:
                    where.append(self.mappings.get(value[0], 'eq')(self.model, k, value[1]).to_peewee())
        return where

    def order(self):
        """
        >>> ImmutableMultiDict([('order', 'id.desc, age.asc')])
        order_by(Book.id.desc(), Book.age.asc())
        """
        order = []
        if 'order' not in self.args:
            return order
        for o in self.args['order'].split(','):
            v = o.split('.')
            if len(v) == 2:
                order.append(getattr(self._meta.fields[v[0]], v[1])())
        return order

    def paginate(self):
        """

        :return:
        """
        page = int(self.args.get(self.page_param, 1))
        return [page, self.paginate_by or 10]

    def query(self):
        query = self.select()
        while len(self.joins) > 0:
            _obj = self.joins.pop()
            query.join(_obj)
        return query.where(*self.where()).order_by(*self.order())

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
