#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'dracarysX'

import math
import json
from flask import request
from flask.views import MethodView
from peewee_rest_query import PeeweeQueryBuilder, PeeweeSerializer
# dracarys import
from .exceptions import APIError, APIError404
from .renders import JSONRender


class SingleObjectMixin(object):

    pk_field = 'id'
    pk_url_kwarg = 'id'

    def get_obj(self):
        args = request.args.to_dict()
        args.update({self.pk_field: request.view_args[self.pk_url_kwarg]})
        self.builder = PeeweeQueryBuilder(self.model, args)
        try:
            obj = self.builder.build().get()
        except self.model.DoesNotExist:
            obj = None
        return obj


class MultiObjectMixin(object):

    context_object_name = 'object_list'
    serializer_class = PeeweeSerializer

    def get_context_data(self):
        self.builder = PeeweeQueryBuilder(self.model, request.args)
        object_list = self.builder.build()
        """
        SELECT COUNT(1) FROM 
            (SELECT `t1`.`id`, `t1`.`name`, `t2`.`name` FROM `Book` AS t1 
                INNER JOIN `Author` AS t2 ON (`t1`.`author_id` = `t2`.`id`) 
            LIMIT 10 OFFSET 0) as wrapped_select
        OperatorError: Duplicate column name 'name'
        """
        # Fix this, so empty select.
        # count = object_list.select().count()
        serializer = self.serializer_class(
            object_list=object_list, 
            select_args=self.builder.parser.select_list
        )
        page, limit = self.builder.paginate
        context = {
            self.context_object_name: serializer.data(),
            'page': page,
            'limit': limit,
            # 'count': count
        }
        # max_page = int(math.ceil(float(count) / limit))
        # context['max_page'] = max_page
        return context


class FormMixin(object):

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


class DetailMixin(SingleObjectMixin):

    serializer_class = PeeweeSerializer

    def _detail(self, obj=None, **kwargs):
        obj = obj or self.get_obj()
        if obj is None:
            raise APIError404()
        serializer = self.serializer_class(obj=obj, select_args=self.builder.parser.select_list)
        return serializer.data()


class DetailView(DetailMixin, MethodView):

    def get(self):
        return self._detail()


class ListMixin(MultiObjectMixin):

    def _list(self, **kwargs):
        context = self.get_context_data()
        return context


class ListView(ListMixin, MethodView):

    def get(self):
        return self._list()


class CreateMixin(FormMixin):

    def _create(self, **kwargs):
        self.obj = None
        form = self.get_form(obj=self.obj)
        if not form.validate():
            return self.form_invalid()
        obj = self.form_valid()
        return {'id': obj.id}


class CreateView(CreateMixin, MethodView):

    def post(self):
        return self._create()


class UpdateMixin(FormMixin):

    def _update(self, **kwargs):
        obj = self.get_obj()
        form = self.get_form(obj)
        if not form.validate():
            return self.form_invalid()
        obj = self.form_valid()
        return {'id': obj.id}


class UpdateView(UpdateMixin, MethodView):

    def put(self):
        return self._update()


class DeleteMixin(FormMixin, SingleObjectMixin):

    def _delete(self, **kwargs):
        obj = self.get_obj()
        obj.delete_instance()
        return JSONRender(message=u'delete success.')


class DeleteView(DeleteMixin, MethodView):

    def delete(self):
        return self._delete()


class APIMethodView(DetailMixin, ListMixin, CreateMixin, UpdateMixin, DeleteMixin, MethodView):

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
