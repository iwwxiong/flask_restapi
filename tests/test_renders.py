#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
# dracarys import
from tests import BaseTestCase
from dracarys.core.renders import JSONRender


class TestJSONRender(BaseTestCase):
    """

    """
    def setUp(self):
        self.content = JSONRender(code=1, message='Bad Request')

    def test_render(self):
        self.assertEqual(self.content.render(), '{"status": {"message": "Bad Request", "code": 1}, "data": []}')


if __name__ == '__main__':
    unittest.main()