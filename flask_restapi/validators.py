# -*-coding: utf-8 -*-
__author__ = 'dracarysX'

from peewee import Model
from wtforms.validators import ValidationError
from wtforms.compat import string_types
# dracarys import
from .model import UUID_REGEXP


class UniqueValidation(ValidationError):
    """
    unique validation.
    """
    def __init__(self, message='', *args, **kwargs):
        ValidationError.__init__(self, message, *args, **kwargs)


class Unique(object):
    """
    Validators of the peewee model unique.
    >>> Unique(model, field_name, message)
    """
    field_flags = ('unique', )

    def __init__(self, field, model=None, message=u''):
        """

        :param field:
        :param model: peewee model object.
        :param message:
        :return:
        """
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        try:
            model = form.meta.model
        except TypeError:
            model = self.model
        if model is None:
            raise ValidationError(u'model is required.')
        if form.obj is None or field.data != getattr(form.obj, self.field):
            count = model.select().where(model._meta.fields[self.field] == field.data).count()
            if count > 0:
                raise UniqueValidation(self.message)


class Foreign(object):
    """
    Validators of the peewee ForeignKey
    """
    field_flags = ('foreign', )

    def __init__(self, model, message=None):
        self.model = model
        self.message = message or 'must be peewee model instance or int or uuid string.'

    def __call__(self, form, field):
        if isinstance(field.data, Model):
            return
        if isinstance(field.data, string_types) and UUID_REGEXP.search(field.data):
            try:
                obj = self.model.get(uuid=field.data)
            except self.model.DoesNotExist:
                raise ValidationError(self.message)
            field.data = obj
            return
        try:
            obj = self.model.get(id=field.data)
        except self.model.DoesNotExist:
            raise ValidationError(self.message)
        field.data = obj
        return