# -*-coding: utf-8 -*-
__author__ = 'dracarysX'

from peewee import Model
from wtforms import Field, StringField
from wtforms.compat import text_type
# dracarys import
from .db import UUID_REGEXP


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
