#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
# dracarys import
from tests import BaseTestCase
from dracarys.core.app import APIFlask
from dracarys.core.exceptions import APIError


app = APIFlask(__name__)
app.config['TESTING'] = True


@app.route('/json_view')
def json_view():
    return {'test': True}


@app.route('/string_view')
def string_view():
    """

    :rtype : object
    """
    return 'string'


@app.route('/api_exception')
def api_exception():
    raise APIError(code=1, message='test api exception.')


class APIFlaskTests(BaseTestCase):
    """

    """
    def test_json_view(self):
        with app.test_client() as client:
            response = client.get('/json_view')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.get_data().decode('utf8'))
            self.assertTrue(data['data']['test'])

    def test_string_view(self):
        with app.test_client() as client:
            response = client.get('/string_view')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.get_data().decode('utf8'))
            self.assertEqual(data['data'], 'string')

    def test_api_exception(self):
        with app.test_client() as client:
            response = client.get('/api_exception')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.get_data().decode('utf8'))
            self.assertEqual(data['status']['code'], 1)