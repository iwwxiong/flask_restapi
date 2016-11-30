#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
# dracarys import
from dracarys.core.utils import register_api
from .views import AuthorView

author_blueprint = Blueprint('authors', __name__, url_prefix='/authors')
# 注册路由
register_api(bp=author_blueprint, view=AuthorView, endpoint='authors', pk='author_id')
