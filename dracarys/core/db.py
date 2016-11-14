# -*-coding: utf-8 -*-

from peewee import Model
from peewee import CharField
from dracarys import db


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