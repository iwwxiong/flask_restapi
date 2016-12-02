# -*-coding: utf-8 -*-
__author__ = 'dracarysX'

from peewee import Model
from wtforms.validators import ValidationError
# dracarys import
from .db import UUID_REGEXP


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
        count = model.select().where(model._meta.fields[self.field] == field.data).count()
        if count > 0:
            raise UniqueValidation(self.message)


class Foreign(object):
    """
    Validators of the peewee ForeignKey
    """
    field_flags = ('foreign', )

    def __init__(self, message=u''):
        self.message = message

    def __call__(self, form, field):
        if not isinstance(field.data, Model) and not UUID_REGEXP.search(field.data):
            try:
                int(field.data)
            except TypeError:
                raise ValidationError(self.message)
            return
        return ValidationError(self.message)