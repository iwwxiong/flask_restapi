# -*-coding: utf-8 -*-

import re
from peewee import Model
from peewee import CharField
from dracarys import db


UUID_REGEXP = re.compile(r'^[0-9a-zA-Z]{32}$')


class BaseModel(Model):
    class Meta:
        database = db


def _uuid():
    import uuid
    return uuid.uuid4().hex


class UUIDBaseModel(BaseModel):
    """
    自动添加uuid(高并发可能产生问题，暂忽略)
    """
    uuid = CharField(default=_uuid, unique=True)