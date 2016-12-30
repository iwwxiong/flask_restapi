#! /usr/bin/env python
# -*- coding: utf-8 -*-

# flask_restapi import
from tests import BaseTestCase
from flask_restapi.renders import JSONRender


class JSONRenderTests(BaseTestCase):
    """

    """
    def setUp(self):
        self.content = JSONRender(code=1, message='Bad Request')

    def test_render(self):
        self.assertEqual(self.content.render(), '{"status": {"message": "Bad Request", "code": 1}, "data": []}')

