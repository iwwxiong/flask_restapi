#! /usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import *
from flask_restapi.model import UUIDBaseModel


class Author(UUIDBaseModel):
    """
    Author model
    """
    id = PrimaryKeyField()
    name = CharField(max_length=50, unique=True)
    age = IntegerField(default=0)

    class Meta:
        db_table = 'Author'

    def __repr__(self):
        return u'<Author {}>'.format(self.name)
