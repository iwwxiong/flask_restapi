#! /usr/bin/env python
# -*- coding: utf-8 -*-


class BaseCondition(object):
    """

    """
    __name__ = 'base'

    def __init__(self, model, field=None, value=None):
        self.model = model
        self.field = field
        self.value = value

    @property
    def field_obj(self):
        return self.model._meta.fields[self.field]

    def to_peewee(self):
        return [self.field_obj == self.value]


class Eq(BaseCondition):
    """

    """
    __name__ = 'eq'


class Neq(BaseCondition):
    """

    """
    __name__ = 'neq'

    def to_peewee(self):
        return [self.field_obj != self.value]


class Gt(BaseCondition):
    """

    """
    __name__ = 'gt'

    def to_peewee(self):
        return [self.field_obj > self.value]


class Gte(BaseCondition):
    """

    """
    __name__ = 'gte'

    def to_peewee(self):
        return [self.field_obj >= self.value]


class Lt(BaseCondition):
    """

    """
    __name__ = 'lt'

    def to_peewee(self):
        return [self.field_obj < self.value]


class Lte(BaseCondition):
    """

    """
    __name__ = 'lte'

    def to_peewee(self):
        return [self.field_obj <= self.value]


class Like(BaseCondition):
    """

    """
    __name__ = 'like'

    def to_peewee(self):
        return [self.field_obj % self.value]


class ILike(BaseCondition):
    """

    """
    __name__ = 'ilike'

    def to_peewee(self):
        return [self.field_obj ** self.value]


class In(BaseCondition):
    """

    """
    __name__ = 'in'

    def to_peewee(self):
        return [self.field_obj << self.value]


mappings = {
    'eq': Eq,
    'neq': Neq,
    'gt': Gt,
    'gte': Gte,
    'lt': Lt,
    'lte': Lte,
    'like': Like,
    'ilike': ILike,
    'in': In
}