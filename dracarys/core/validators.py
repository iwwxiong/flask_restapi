# -*-coding: utf-8 -*-
__author__ = 'dracarysX'

from wtforms.validators import ValidationError


class UniqueValidation(Exception):
    """
    unique validation.
    """
    def __init__(self, message='', *args, **kwargs):
        Exception.__init__(self, message, *args, **kwargs)


class Unique(object):
    """
    Validators of the peewee model unique.
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
        count = model.select().where(model._meta.fields['name'] == field.data).count()
        if count > 0:
            raise UniqueValidation(self.message)


class Foreign(object):
    """
    Validators of the peewee ForeignKey
    """
    field_flags = ('foreign', )

    def __init__(self):
        pass