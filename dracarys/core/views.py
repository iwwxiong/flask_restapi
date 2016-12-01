#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = '10000573'

import math
from flask.views import MethodView
# dracarys import
from exceptions import APIError404
from .parsers import QueryParser
from .serializers import PeeweeSerializer
from .querys import PeeweeObjectMixin


class SingleObjectMixin(PeeweeObjectMixin):
    """

    """
    pk_field = 'id'
    pk_url_kwarg = 'id'

    def _where(self):
        return [self.model._meta.fields[self.pk_field] == self.view_args[self.pk_url_kwarg]]

    def get_obj(self):
        try:
            obj = self.get_query(where=self._where())[0]
        except IndexError:
            obj = None
        self.obj = obj
        return self.obj


class FormMixin(SingleObjectMixin):
    """

    """
    form_class = None


class MultiObjectMixin(PeeweeObjectMixin):
    """

    """
    context_object_name = 'object_list'
    serializer_class = PeeweeSerializer

    def get_context_data(self):
        object_list = self.get_query_paginate()
        count = self.count()
        serializer = self.serializer_class(object_list=object_list, select_args=self._select_args)
        page, limit = self.paginate()
        context = {
            self.context_object_name: serializer.data(),
            'page': page,
            'limit': limit,
            'count': count
        }
        max_page = int(math.ceil(float(count)/limit))
        context['max_page'] = max_page
        return context


class DetailMixin(SingleObjectMixin):

    serializer_class = PeeweeSerializer

    def _detail(self):
        obj = self.get_obj()
        if obj is None:
            raise APIError404()
        serializer = self.serializer_class(obj=obj, select_args=self._select_args)
        return serializer.data()


class DetailView(DetailMixin, MethodView):
    """

    """
    def get(self):
        return self._detail()


class ListMixin(MultiObjectMixin):
    """
    """
    def _list(self):
        context = self.get_context_data()
        return context


class ListView(ListMixin, MethodView):
    """

    """
    def get(self):
        return self._list()


class CreateMixin(FormMixin):
    """
    """
    def _create(self):
        pass


class CreateView(CreateMixin, MethodView):
    """

    """
    def post(self):
        pass


class UpdateMixin(FormMixin):
    """
    """
    def _update(self):
        pass


class UpdateView(UpdateMixin, MethodView):
    """

    """
    def put(self):
        pass


class DeleteMixin(FormMixin):
    """
    """
    def _delete(self):
        pass


class DeleteView(DeleteMixin, MethodView):
    """
    """
    def delete(self):
        pass


class APIMethodView(DetailMixin, ListMixin, CreateMixin, UpdateMixin, DeleteMixin, MethodView):
    """

    """
    def get(self, **kwargs):
        if self.pk_url_kwarg in kwargs:
            return self._detail()
        return self._list()

    def post(self):
        return self._create()

    def put(self, **kwargs):
        return self._update()

    def delete(self, **kwargs):
        return self._delete()