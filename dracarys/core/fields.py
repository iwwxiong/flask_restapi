# -*-coding: utf-8 -*-
__author__ = 'dracarysX'

from wtforms import Field, StringField


class StringField(StringField):
    """

    """
    def process_formdata(self, valuelist):
        # fix issue https://github.com/wtforms/wtforms/issues/291
        if valuelist:
            self.data = valuelist[0]


class ForeignField(Field):
    """
    a text field for peewee ForeignKeyField.
    >>> f = ForeignField()
    """
    def __init__(self, label=None, validators=None, **kwargs):
        super(ForeignField, self).__init__(label, validators, **kwargs)
