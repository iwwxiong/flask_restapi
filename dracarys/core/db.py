# -*-coding: utf-8 -*-

from peewee import Model
from dracarys import db


class BaseModel(Model):
    class Meta:
        database = db
