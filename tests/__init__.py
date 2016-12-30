#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
# flask_restapi import


def clear_tables(model):
    """
    清空表数据
    :return:
    """
    q = model.delete()
    q.execute()
    return


class BaseTestCase(unittest.TestCase):
    """

    """
    @classmethod
    def setUpClass(cls):
        pass


class DBTestCase(BaseTestCase):
    """
    涉及数据库测试，继承此class
    """
    @staticmethod
    def remove_db_file():
        import os
        if os.path.exists('flask_restapi.db'):
            os.remove('flask_restapi.db')
        return

    @classmethod
    def setUpClass(cls):
        pass
        # 考虑清空测试表数据

    @classmethod
    def tearDownClass(cls):
        cls.remove_db_file()


