#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
# dracarys import
from dracarys import create_app
from scripts import create_tables, drop_tables


class BaseTestCase(unittest.TestCase):
    """

    """
    @classmethod
    def setUpClass(cls):
        # 载入测试配置
        app = create_app(testing=True)
        cls.app = app


class DBTestCase(BaseTestCase):
    """
    涉及数据库测试，继承此class
    """
    @classmethod
    def setUpClass(cls):
        # 初始化数据库
        create_tables()

    @classmethod
    def tearDownClass(cls):
        drop_tables()
