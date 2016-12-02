# -*- coding: utf-8 -*-

from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange
# dracarys import
from dracarys.core.forms import PeeweeForm
from dracarys.core.validators import Unique
from dracarys.author.models import Author


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

