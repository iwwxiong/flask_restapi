#! /usr/bin/env python
# -*- coding: utf-8 -*-


def create_tables():
    """
    创建数据库table
    :return:
    """
    from dracarys.author.models import Author
    from dracarys.book.models import Book

    Author.create_table()
    Book.create_table()
    return
