#! /usr/bin/env python
# -*- coding: utf-8 -*-

# flask_restapi import
from peewee import *
from tests import BaseTestCase
from flask_restapi.conditions import *
from flask_restapi.model import UUIDBaseModel


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


class EqTests(BaseTestCase):
    """

    """
    def test_to_peewee(self):
        eq = Eq(model=Author, field='name', value='wwxiong')
        self.assertEqual(eq.to_peewee(), [Author.name == 'wwxiong'])


class NeqTests(BaseTestCase):
    """

    """
    def test_to_peewee(self):
        neq = Neq(model=Author, field='name', value='wwxiong')
        self.assertEqual(neq.to_peewee(), [Author.name != 'wwxiong'])


class GtTests(BaseTestCase):
    """

    """
    def test_to_peewee(self):
        gt = Gt(model=Author, field='age', value=25)
        self.assertEqual(gt.to_peewee(), [Author.age > 25])


class GteTests(BaseTestCase):
    """

    """
    def test_to_peewee(self):
        gte = Gte(model=Author, field='age', value=25)
        self.assertEqual(gte.to_peewee(), [Author.age >= 25])


class LtTests(BaseTestCase):
    """

    """
    def test_to_peewee(self):
        lt = Lt(model=Author, field='age', value=25)
        self.assertEqual(lt.to_peewee(), [Author.age < 25])


class LteTests(BaseTestCase):
    """

    """
    def test_to_peewee(self):
        lte = Lte(model=Author, field='age', value=25)
        self.assertEqual(lte.to_peewee(), [Author.age <= 25])


class LikeTests(BaseTestCase):
    """

    """
    def test_to_peewee(self):
        like = Like(model=Author, field='name', value='dracarys')
        self.assertEqual(like.to_peewee(), [Author.name % 'dracarys'])


class ILikeTests(BaseTestCase):
    """

    """
    def test_to_peewee(self):
        ilike = ILike(model=Author, field='name', value='dracarys')
        self.assertEqual(ilike.to_peewee(), [Author.name ** 'dracarys'])


class InTests(BaseTestCase):
    """

    """
    def test_to_peewee(self):
        _in = In(model=Author, field='age', value=[25, 26])
        self.assertEqual(_in.to_peewee(), [Author.age << [25, 26]])

