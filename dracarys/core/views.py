#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = '10000573'

import math
import json
from flask import request
from flask.views import MethodView
# dracarys import
from exceptions import APIError, APIError404
from .serializers import PeeweeSerializer
from .querys import PeeweeObjectMixin
from .renders import JSONRender


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
        return obj


class FormMixin(object):
    """

    """
    form_class = None

    def get_form_class(self):
        return self.form_class

    def get_form(self, obj=None):
        form = self.form_class(formdata=request.form, obj=obj)
        self.form_obj = form
        return self.form_obj

    def form_valid(self):
        """
        save form instance
        """
        obj = self.form_obj.save()
        return obj

    def form_invalid(self):
        """
        render response
        """
        errors = self.form_obj.errors
        raise APIError(code=409, message='; '.join(['%s: %s' % (k, '; '.join(v)) for k, v in errors.items()]))


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

    def _detail(self, obj=None, **kwargs):
        obj = obj or self.get_obj()
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
    def _list(self, **kwargs):
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
    def _create(self, **kwargs):
        self.obj = None
        form = self.get_form(obj=self.obj)
        if not form.validate():
            return self.form_invalid()
        obj = self.form_valid()
        return {'id': obj.id}


class CreateView(CreateMixin, MethodView):
    """

    """
    def post(self):
        return self._create()


class UpdateMixin(FormMixin):
    """
    """
    def _update(self, **kwargs):
        obj = self.get_obj()
        form = self.get_form(obj)
        if not form.validate():
            return self.form_invalid()
        obj = self.form_valid()
        return {'id': obj.id}


class UpdateView(UpdateMixin, MethodView):
    """

    """
    def put(self):
        return self._update()


class DeleteMixin(FormMixin, SingleObjectMixin):
    """
    """
    def _delete(self, **kwargs):
        obj = self.get_obj()
        # obj.delete().execute()
        obj.delete_instance()
        return JSONRender(message=u'删除成功。')


class DeleteView(DeleteMixin, MethodView):
    """
    """
    def delete(self):
        return self._delete()


class APIMethodView(DetailMixin, ListMixin, CreateMixin, UpdateMixin, DeleteMixin, MethodView):
    """

    """
    def get(self, **kwargs):
        if self.pk_url_kwarg in kwargs:
            return self._detail(**kwargs)
        return self._list(**kwargs)

    def post(self):
        return self._create()

    def put(self, **kwargs):
        return self._update(**kwargs)

    def delete(self, **kwargs):
        return self._delete(**kwargs)