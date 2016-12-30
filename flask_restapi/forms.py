#! /usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import Model
from wtforms import Form


class PeeweeFormException(Exception):
    """
    """
    def __init__(self, message=''):
        super(self.__class__, self).__init__()
        self.message = message


class PeeweeForm(Form):
    """
    form for peewee model instance. # 暂不实现类似django ModelForm功能
    """
    def __init__(self, formdata=None, obj=None, data=None, *args, **kwargs):
        super(PeeweeForm, self).__init__(formdata=formdata, obj=obj, data=data, *args, **kwargs)
        if obj is not None and not isinstance(obj, Model):
            raise PeeweeFormException(u'obj must None or peewee model instance.')
        self.obj = obj
        self._validate = False

    def validate(self):
        validate = super(PeeweeForm, self).validate()
        self._validate = validate
        return self._validate

    def create(self):
        if not hasattr(self.meta, 'model'):
            raise PeeweeFormException(u'need model')
        obj = self.meta.model()
        self.populate_obj(obj)
        self.obj = obj
        return self.obj

    def update(self):
        self.populate_obj(obj=self.obj)
        return self.obj

    def _save_instance(self):
        if not self._validate:
            raise PeeweeFormException(u'validate is false.')
        self.obj = self.create() if self.obj is None else self.update()
        self.obj.save()
        return self.obj

    def save(self):
        obj = self._save_instance()
        return obj