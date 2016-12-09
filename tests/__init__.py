#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
# dracarys import
from dracarys import create_app


class BaseTestCase(unittest.TestCase):
    """

    """
    @classmethod
    def setUpClass(cls):
        # 载入测试配置
        app = create_app(testing=True)
        from dracarys.core.db import db
        print db.database


class DBTestCase(BaseTestCase):
    """
    涉及数据库测试，继承此class
    """
    @classmethod
    def setUpClass(cls):
        # 初始化数据库
        pass