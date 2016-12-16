#! /usr/bin/env python
# -*- coding: utf-8 -*-

# dracarys import
from tests import DBTestCase
from dracarys.author.models import Author
from dracarys.book.models import Book
from dracarys.core.serializers import PeeweeSerializer


def init_data():
    """
    初始化数据
    """
    Author(name='wwxiong', age=24).save()
    Author(name='dracarys', age=100).save()
    Book(name='python', author=Author.get(name='wwxiong')).save()
    Book(name='javascript', author=Author.get(name='dracarys')).save()
    return


class PeeweeSerializerTests(DBTestCase):
    """

    """
    @classmethod
    def setUpClass(cls):
        super(PeeweeSerializerTests, cls).setUpClass()
        init_data()
        cls.a1 = Author.get(name='wwxiong')
        cls.a2 = Author.get(name='dracarys')
        cls.b1 = Book.get(name='python')
        cls.b2 = Book.get(name='javascript')

    def test_serializer_without_select(self):
        searializer = PeeweeSerializer(obj=self.a1)
        data = searializer.data()
        self.assertEqual(data['name'], 'wwxiong')

    def test_serializer_with_select(self):
        searializer = PeeweeSerializer(obj=self.a2, select_args=['id', 'name'])
        data = searializer.data()
        self.assertEqual(data['name'], 'dracarys')
        self.assertIn('id', data)

    def test_foreign_serializer_without_select(self):
        searializer = PeeweeSerializer(obj=self.b1)
        data = searializer.data()
        self.assertEqual(data['name'], 'python')
        self.assertEqual(data['author'], self.a1.id)

    def test_foreign_serializer_with_select(self):
        searializer = PeeweeSerializer(obj=self.b2, select_args=['id', 'name', ['author.name', 'author.age']])
        data = searializer.data()
        self.assertEqual(data['name'], 'javascript')
        self.assertEqual(data['author']['age'], 100)

    def test_serializer_object_list_without_select(self):
        serializer = PeeweeSerializer(object_list=Author.select().where(Author.age == 24))
        data = serializer.data()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'wwxiong')

    def test_serializer_object_list_with_select(self):
        serializer = PeeweeSerializer(object_list=Author.select().where(Author.age == 100), select_args=['name'])
        data = serializer.data()
        self.assertEqual(len(data), 1)
        self.assertNotIn('id', data[0])
        self.assertEqual(data[0]['name'], 'dracarys')

