#! /usr/bin/env python
# -*- coding: utf-8 -*-

# flask_restapi import
from peewee import *
from tests import DBTestCase
from flask_restapi.serializers import PeeweeSerializer
from flask_restapi.model import UUIDBaseModel
from flask_restapi.app import APIFlask
from flask_restapi.db import Database
from tests import clear_tables

app = APIFlask(__name__)
app.config['TESTING'] = True
db = Database(app, app.config.get('DB_ENGINE')(**app.config['DATABASE']))


class Author(UUIDBaseModel):
    """
    作者
    """
    id = PrimaryKeyField()
    name = CharField(max_length=50, unique=True)
    age = IntegerField(default=0)

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


class PeeweeSerializerTests(DBTestCase):
    """

    """
    a1 = Author(name='wwxiong', age=24)
    a2 = Author(name='dracarys', age=100)
    b1 = Book(name='python', author=a1)
    b2 = Book(name='javascript', author=a2)

    def test_serializer_without_select(self):
        searializer = PeeweeSerializer(obj=self.a1)
        data = searializer.data()
        self.assertEqual(data['name'], 'wwxiong')

    def test_serializer_with_select(self):
        searializer = PeeweeSerializer(obj=self.a2, select_args=['name'])
        data = searializer.data()
        self.assertEqual(data['name'], 'dracarys')

    def test_foreign_serializer_without_select(self):
        searializer = PeeweeSerializer(obj=self.b1)
        data = searializer.data()
        self.assertEqual(data['name'], 'python')

    def test_foreign_serializer_with_select(self):
        searializer = PeeweeSerializer(obj=self.b2, select_args=['name', ['author.name', 'author.age']])
        data = searializer.data()
        self.assertEqual(data['name'], 'javascript')
        self.assertEqual(data['author']['age'], 100)

    def test_serializer_object_list_without_select(self):
        serializer = PeeweeSerializer(object_list=[self.a1])
        data = serializer.data()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'wwxiong')

    def test_serializer_object_list_with_select(self):
        serializer = PeeweeSerializer(object_list=[self.a2], select_args=['name'])
        data = serializer.data()
        self.assertEqual(len(data), 1)
        self.assertNotIn('id', data[0])
        self.assertEqual(data[0]['name'], 'dracarys')
