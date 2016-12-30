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
    作者表单
    """
    name = StringField(
        label=u'姓名',
        validators=[DataRequired(), Length(max=50), Unique(
            field='name',
            message=u'该作者姓名已存在。'
        )]
    )
    age = IntegerField(
        label=u'年龄',
        validators=[DataRequired(), NumberRange(0, 150)]
    )

    class Meta:
        model = Author

