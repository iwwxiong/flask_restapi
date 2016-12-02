#! /usr/bin/env python
# -*- coding: utf-8 -*-

from wtforms import StringField
from wtforms.validators import DataRequired, Length
# dracarys import
from dracarys.core.validators import Unique, Foreign
from dracarys.core.fields import ForeignField
from dracarys.core.forms import PeeweeForm
from dracarys.author.models import Author
from dracarys.book.models import Book


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
        validators=[DataRequired(), Foreign(message=u'必须是Author实例，Author.id或者Author.uuid')],
        model=Author,
        display_field='name',
    )

    class Meta:
        model = Book
