#! /usr/bin/env python
# -*- coding: utf-8 -*-

from dracarys.author.models import Author
from dracarys.book.models import Book


def create_tables():
    """
    创建数据库table
    :return:
    """
    Author.create_table()
    Book.create_table()
    return


def drop_tables():
    """
    删除数据表
    :return:
    """
    Author.drop_table()
    Book.drop_table()
    return


def clear_tables(model):
    """
    清空表数据
    :return:
    """
    q = model.delete()
    q.execute()
    return
