#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask import request, g, current_app
# dracarys import
from dracarys.author.models import Author
from dracarys.core.querys import PeeweeObjectMixin
from dracarys.core.views import APIMethodView


class AuthorView(PeeweeObjectMixin, APIMethodView):
    """

    """
    model = Author
    paginate_by = 10

    def get(self):
        object_list = self.get_query()
        return [obj.id for obj in object_list]

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
