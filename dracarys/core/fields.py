# -*-coding: utf-8 -*-
__author__ = 'dracarysX'

from peewee import Model
from wtforms import Field
from wtforms.compat import text_type
# dracarys import
from .db import UUID_REGEXP


class ForeignField(Field):
    """
    a text field for peewee ForeignKeyField.
    >>> f = ForeignField(model=Book, display_field='name')  # this will display book.name
    """
    def __init__(self, label=None, validators=None, model=None, display_field=None, **kwargs):
        super(ForeignField, self).__init__(label, validators, **kwargs)
        self.model = model
        self.display_field = display_field

    def _value(self):
        if self.raw_data:
            return self.raw_data[0]
        elif self.data is not None:
            return text_type(self.data)
        else:
            return ''

    def process_formdata(self, valuelist):
        if valuelist:
            value = valuelist[0]
            if isinstance(value, Model):
                self.data = getattr(value, self.display_field)
                self._obj = value
                return
            if isinstance(value, str) and UUID_REGEXP.search(value):
                try:
                    obj = self.model.get(uuid=value)
                except self.model.DoesNotExist:
                    raise ValueError(self.gettext('Not a valid uuid string.'))
                self._obj = obj
                self.data = getattr(obj, self.display_field)
                return
            try:
                obj = self.model.get(id=value)
            except self.model.DoesNotExist:
                raise ValueError(self.gettext('Not a integer number.'))
            self._obj = obj
            self.data = getattr(obj, self.display_field)
            return

    def populate_obj(self, obj, name):
        return setattr(obj, name, self._obj.id)