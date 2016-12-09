#! /usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import *
from dracarys.core.model import UUIDBaseModel


class Author(UUIDBaseModel):
    """
    作者
    """
    id = PrimaryKeyField()
    name = CharField(max_length=50, unique=True)
    age = IntegerField(default=0, unique=True)

    class Meta:
        db_table = 'Author'

    def __repr__(self):
        return u'<Author {}>'.format(self.name)

