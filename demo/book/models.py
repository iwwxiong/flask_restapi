#! /usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import *
# flask_restapi import
from flask_restapi.model import UUIDBaseModel
from ..author.models import Author


class Book(UUIDBaseModel):
    """
    书籍
    """
    id = PrimaryKeyField()
    name = CharField(max_length=255, unique=True)
    author = ForeignKeyField(Author, related_name='books')

    class Meta:
        db_table = 'Book'

    def __repr__(self):
        return u'<Book {}>'.format(self.name)


