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
    Book form
    """
    name = StringField(
        label='Name',
        validators=[DataRequired(), Length(max=255), Unique(
            field='name',
            message='book is exist'
        )]
    )
    author = ForeignField(
        label='Author',
        validators=[DataRequired(), Foreign(model=Author, message='author not exist')],
    )

    class Meta:
        model = Book
