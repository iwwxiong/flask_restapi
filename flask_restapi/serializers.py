#! /usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import ForeignKeyField
# dracarys import
from .utils import set_dict


class BaseSerializer(object):
    """
    base serializer
    """
    def __init__(self, obj=None, object_list=None, select_args=None):
        """
        >>> obj = Book.get(id=1)
        >>> object_list = Book.select()
        >>> select_args = [id, name, [author.id, author.name, author.age, [author.school.id, author.school.name]]]
        >>> serializer = BaseSerializer(obj=obj, select_args=select_args)
        {
            'id': 1,
            'name': 'javascript',
            'author': {
                'id': 1,
                'name': 'dracarysX',
                'school': {
                    'id': 1,
                    'name': 'Stanford'
                }
            }
        }
        """
        self.obj = obj
        self.object_list = object_list
        self.select_args = select_args

    def _obj_serializer(self, obj):
        raise NotImplementedError()

    def serializer(self, obj):
        """
        single obj serializer.
        """
        if self.select_args is None:
            return self._obj_serializer(obj)
        d = {}

        def _get_instance(_obj, _key):
            """
            >>> _get_instance(book, 'author.school')
            author
            """
            k = _key.split('.')
            k.reverse()
            instance = _obj
            while len(k) > 0:
                v = k.pop()
                if instance is not None and v in instance._meta.fields:
                    instance = getattr(instance, v)
                else:
                    instance = None
            return instance

        def _serializer(args):
            for arg in args:
                if not isinstance(arg, list):
                    v = arg.rsplit('.', 1)
                    if len(v) == 1:
                        if v[0] in obj._meta.fields:
                            if isinstance(obj._meta.fields[v[0]], ForeignKeyField):
                                d[v[0]] = getattr(obj, '{}_id'.format(v[0]))
                            else:
                                d[v[0]] = getattr(obj, v[0])
                    else:
                        if v[1] == '*':
                            set_dict(d, v[0], self._obj_serializer(_get_instance(obj, v[0])))
                        else:
                            _model = _get_instance(obj, v[0])
                            if v[1] in _model._meta.fields:
                                set_dict(d, arg, getattr(_model, v[1]))
                else:
                    _serializer(arg)

        if len(self.select_args) == 0:
            return self._obj_serializer(obj)
        _serializer(self.select_args)
        return d

    def data(self):
        """
        serializer
        :return: {json object}
        """
        if self.obj is not None:
            return self.serializer(obj=self.obj)
        return [self.serializer(obj=obj) for obj in self.object_list]


class PeeweeSerializer(BaseSerializer):
    """
    serializer for peewee object instance.
    """
    def _obj_serializer(self, obj):
        if hasattr(obj, 'serializer'):
            return getattr(obj, 'serializer')
        return {k: getattr(obj, k if not isinstance(v, ForeignKeyField) else '%s_id' % k)
                for k, v in obj.__class__._meta.fields.items()}
