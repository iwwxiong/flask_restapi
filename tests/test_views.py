#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from peewee import *
from wtforms import IntegerField as WTFIntegerField
from wtforms.validators import DataRequired, Length, NumberRange
# flask_restapi import
from tests import DBTestCase
from tests import clear_tables
from flask_restapi.views import *
from flask_restapi.app import APIFlask
from flask_restapi.utils import register_api
from flask_restapi.model import UUIDBaseModel
from flask_restapi.fields import StringField
from flask_restapi.forms import PeeweeForm
from flask_restapi.validators import Unique
from flask_restapi.db import Database

app = APIFlask(__name__)
app.config['TESTING'] = True
db = Database(app, app.config.get('DB_ENGINE')(**app.config['DATABASE']))


class Author(UUIDBaseModel):
    """
    作者
    """
    id = PrimaryKeyField()
    name = CharField(max_length=50, unique=True)
    age = IntegerField(default=0)

    class Meta:
        db_table = 'Author'

    def __repr__(self):
        return u'<Author {}>'.format(self.name)


class AuthorForm(PeeweeForm):
    """
    作者表单
    """
    name = StringField(
        label=u'姓名',
        validators=[DataRequired(), Length(max=50), Unique(
            field='name',
            message=u'该作者姓名已存在。'
        )]
    )
    age = WTFIntegerField(
        label=u'年龄',
        validators=[DataRequired(), NumberRange(0, 150)]
    )

    class Meta:
        model = Author


class AuthorView(APIMethodView):
    """

    """
    model = Author
    paginate_by = 10
    context_object_name = 'items'
    pk_url_kwarg = 'author_id'
    form_class = AuthorForm


author_blueprint = Blueprint('authors', __name__, url_prefix='/authors')
register_api(bp=author_blueprint, view=AuthorView, endpoint='authors', pk='author_id')
app.register_blueprint(author_blueprint)


class APIMethodViewTests(DBTestCase):
    """

    """
    @classmethod
    def setUpClass(cls):
        super(APIMethodViewTests, cls).setUpClass()
        Author.create_table()

    def setUp(self):
        Author(name='dracarys', age=100).save()

    def tearDown(self):
        clear_tables(Author)

    @classmethod
    def tearDownClass(cls):
        Author.drop_table()
        db.close_db(None)
        super(APIMethodViewTests, cls).tearDownClass()

    def test_get(self):
        with app.test_client() as client:
            response = client.get('/authors')
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['status']['code'], 0)
            self.assertEqual(data['data']['page'], 1)

    def test_get_id(self):
        with app.test_client() as client:
            author_id = Author.get(name='dracarys').id
            response = client.get('/authors/{}'.format(author_id))
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

