#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re


class QueryParser(object):
    """

    """
    model = None
    paginate_by = None
    where_exclude = ['select', 'order', 'page', 'limit']
    page_param = 'page'

    def __init__(self):
        from flask import request
        from .conditions import mappings
        self.args = request.args
        self.view_args = request.view_args
        self.mappings = mappings
        self.joins = set()
        self._select_args = self._args_split(select=self.args['select']) if 'select' in self.args else []

    def _args_split(self, select):
        """
        请求select参数处理
        :param select:
        :return:
        >>> _args_split('id,name,author{id,name,age,school{id,name}}')
        [id, name, [author.id, author.name, author.age, [author.school.id, author.school.name]]]
        """
        _select = []

        def _dispose(s):
            """
            >>> _dispose('id,name,author{id,name,age,school{id,name}},publish{id,name}')
            [id,name,author{id,name,age,school{id,name}},publish{id,name}]
            """
            r = re.compile(r'\w+\{.*?\}\}*')
            ns = r.findall(s)
            ns.extend(filter(None, ''.join(r.split(s)).split(',')))
            return ns

        def _handle_args_split(_s, params, k=None):
            r = re.compile(r'^(?P<key>\w+){(?P<value>.+)}$')
            for index, param in enumerate(params):
                if r.search(param):
                    key, value = r.search(param).groups()
                    if k is not None:
                        key = '%s.%s' % (k, key)
                    _s.append([])
                    _handle_args_split(_s[index], _dispose(value), k=key)
                else:
                    if k is not None:
                        param = '%s.%s' % (k, param)
                    _s.append(param)

        _handle_args_split(_select, _dispose(select))
        return _select

    def select(self):
        """
        >>> select([id, name, [author.id, author.name, author.age, [author.school.id, author.school.name]]])
        [Book.id, Book.name, Author.id, Author.name, Author.age, school.id, school.name]
        """
        def _get_model(o, f):
            """
            >>> _get_model(Book, 'author')
            Author
            """
            new_obj = o
            for v in f.split('.'):
                if new_obj is not  None and v in new_obj._meta.fields:
                    new_obj = new_obj._meta.fields[v].rel_model
                else:
                    new_obj = None
            return new_obj

        def _handel(_params):
            for param in _params:
                if not isinstance(param, list):
                    value = param.rsplit('.', 1)
                    if len(value) == 1:
                        if param in self.model._meta.fields:
                            select.append(self.model._meta.fields[param])
                    else:
                        if value[1] == '*':
                            obj = _get_model(self.model, value[0])
                            self.joins.add(obj)  # 增加链接查询
                            select.append(_get_model(self.model, value[0]))
                        else:
                            obj = _get_model(self.model, value[0])
                            if obj is not None and value[1] in obj._meta.fields:
                                self.joins.add(obj)  # 增加链接查询
                                select.append(obj._meta.fields[value[1]])
                else:
                    _handel(param)

        select = []
        _handel(self._select_args)
        self._select = select

        return self._select

    def where(self):
        """
        >>> where(ImmutableMultiDict([('name', 'dracarysX'), ('age', 'lt.30')]))
        (Book.name == 'dracarysX', Book.age > 30)
        """
        params = {key: value for key, value in self.args.items() if key not in self.where_exclude}
        where = []
        for k, v in params.items():
            if k in self.model._meta.fields:
                value = v.split('.')
                if len(value) == 1:
                    where.append(self.mappings['eq'](self.model, k, v).to_peewee()[0])
                else:
                    where.append(self.mappings.get(value[0], 'eq')(self.model, k, value[1]).to_peewee()[0])
        return where

    def order(self):
        """
        >>> order(ImmutableMultiDict([('order', 'id.desc, age.asc')]))
        order_by(Book.id.desc(), Book.age.asc())
        """
        order = []
        if 'order' not in self.args:
            return order
        for o in self.args['order'].split(','):
            v = o.split('.')
            if len(v) == 2:
                order.append(getattr(self.model._meta.fields[v[0]], v[1])())
        return order

    def paginate(self):
        """

        :return:
        """
        page = int(self.args.get(self.page_param, 1))
        limit = int(self.args['limit']) if 'limit' in self.args else self.paginate_by or 10
        return [page, limit]

    def pre_select(self):
        if 'select' not in self.args:
            return self.model.select()
        return self.model.select(*self.select())