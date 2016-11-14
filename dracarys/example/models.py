# -*-coding: utf-8 -*-

from peewee import *
from dracarys.core.db import UUIDBaseModel


class Author(UUIDBaseModel):
    """
    作者
    """
    id = PrimaryKeyField()
    name = CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'Author'

    def __repr__(self):
        return u'<Author {}>'.format(self.name)


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
