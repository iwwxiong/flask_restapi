# -*- coding: utf-8 -*-

from wtforms import IntegerField
from wtforms.validators import DataRequired, Length, NumberRange
# flask_restapi import
from flask_restapi.fields import StringField
from flask_restapi.forms import PeeweeForm
from flask_restapi.validators import Unique
from .models import Author


class AuthorForm(PeeweeForm):
    """
    author form
    """
    name = StringField(
        label='Name',
        validators=[DataRequired(), Length(max=50), Unique(
            field='name',
            message='author is exist'
        )]
    )
    age = IntegerField(
        label='Age',
        validators=[DataRequired(), NumberRange(0, 150)]
    )

    class Meta:
        model = Author
