#! /usr/bin/env python
# -*- coding: utf-8 -*-

from demo.author.models import Author
from demo.book.models import Book


def create_tables():
    """
    创建数据库table
    :return:
    """
    Author.create_table()
    Book.create_table()
    return



