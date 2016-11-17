# -*- coding: utf-8 -*-

from wtforms import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length
# dracarys import
from dracarys.author.models import Author
from dracarys.core.validators import Unique


class AuthorForm(Form):
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

    class Meta:
        model = Author

