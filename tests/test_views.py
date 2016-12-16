#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
# dracarys import
from tests import DBTestCase
from scripts import clear_tables
from dracarys.core.views import *
from dracarys.author.models import Author
from dracarys.author.forms import AuthorForm
from dracarys.core.app import APIFlask
from dracarys.core.utils import register_api


class AuthorView(APIMethodView):
    """

    """
    model = Author
    paginate_by = 10
    context_object_name = 'items'
    pk_url_kwarg = 'author_id'
    form_class = AuthorForm


app = APIFlask(__name__)
app.config['TESTING'] = True
author_blueprint = Blueprint('authors', __name__, url_prefix='/authors')
register_api(bp=author_blueprint, view=AuthorView, endpoint='authors', pk='author_id')
app.register_blueprint(author_blueprint)


class APIMethodViewTests(DBTestCase):
    """

    """
    def setUp(self):
        Author(name='dracarys', age=100).save()

    def tearDown(self):
        clear_tables(Author)

    def test_get(self):
        with app.test_client() as client:
            response = client.get('/authors')
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['status']['code'], 0)
            self.assertEqual(data['data']['page'], 1)

    def test_get_id(self):
        with app.test_client() as client:
            response = client.get('/authors/1')
            data = response.get_json()
            self.assertEqual(data['data']['age'], 100)

    def test_post(self):
        with app.test_client() as client:
            response = client.post('/authors', data={'name': 'wwxiong', 'age': 24})
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['status']['code'], 0)

    def test_put(self):
        author = Author.get(name='dracarys')
        with app.test_client() as client:
            response = client.put('/authors/{}'.format(author.id), data={'age': 25})
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['status']['code'], 0)
            self.assertEqual(data['data']['id'], author.id)

    def test_delete(self):
        author = Author.get(name='dracarys')
        with app.test_client() as client:
            response = client.delete('/authors/{}'.format(author.id))
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['status']['code'], 0)

