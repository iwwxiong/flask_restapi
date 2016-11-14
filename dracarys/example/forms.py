# -*-coding: utf-8 -*-

from wtforms import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length

from dracarys.example.models import Author, Book
from dracarys.core.validators import Unique
from dracarys.core.fields import ForeignField


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


class BookForm(Form):
    """
    书籍表单
    """
    name = StringField(
        label=u'姓名',
        validators=[DataRequired(), Length(max=255), Unique(
            model=Book,
            field='name',
            message=u'该书籍名称已存在。'
        )]
    )
    author = ForeignField(
        label=u'作者',
        validators=[DataRequired(), ]
    )

    class Meta:
        model = Book