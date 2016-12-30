#! /usr/bin/env python
# -*- coding: utf-8 -*-

from wtforms.validators import DataRequired, Length
# flask_restapi import
from flask_restapi.validators import Unique, Foreign
from flask_restapi.fields import ForeignField, StringField
from flask_restapi.forms import PeeweeForm
from ..author.models import Author
from .models import Book


class BookForm(PeeweeForm):
    """
    书籍表单
    """
    name = StringField(
        label=u'姓名',
        validators=[DataRequired(), Length(max=255), Unique(
            field='name',
            message=u'该书籍名称已存在。'
        )]
    )
    author = ForeignField(
        label=u'作者',
        validators=[DataRequired(), Foreign(model=Author, message=u'作者不存在')],
    )

    class Meta:
        model = Book
