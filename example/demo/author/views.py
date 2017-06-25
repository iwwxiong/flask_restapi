#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask import request, g, current_app
# dracarys import
from flask_restapi.views import APIMethodView
from .models import Author
from .forms import AuthorForm


class AuthorView(APIMethodView):

    model = Author
    paginate_by = 10
    context_object_name = 'items'
    pk_url_kwarg = 'author_id'
    form_class = AuthorForm
