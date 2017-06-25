#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
from peewee import Model, CharField
# dracarys import
from .db import db as database

UUID_REGEXP = re.compile(r'^[0-9a-zA-Z]{32}$')


def _uuid():
    import uuid
    return uuid.uuid4().hex


class BaseModel(Model):
    class Meta:
        database = database


class UUIDBaseModel(BaseModel):
    """
    auto uuid field
    """
    uuid = CharField(default=_uuid, unique=True)
