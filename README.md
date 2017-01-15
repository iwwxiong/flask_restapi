# Flask restAPI开发脚手架

一款简易的restapi开发脚手架。服务端采用flask，orm使用peewee，表单使用wtform。都是轻量级框架，简单易学。实现自定义查询[查询API参考网站](http://postgrest.com/api/reading/)，表单保存，模型数据序列化，APIMethodView（实现get， post， put，delete操作），异常错误处理等。

## 准备&安装

使用`virtualenv`部署环境

    > git clone https://github.com/dracarysX/flask_restapi.git
    > cd flask_restapi
    > virtualenv --no-site-packages venv
    > source venv/bin/activate
    > python setup.py install

暂未推送到公共仓库中，所以目前使用源码安装。

## 测试

    > python setup.py test

## 案列演示

[demo介绍](https://github.com/dracarysX/flask_restapi/tree/master/demo/README.md)

## 查询API

查询姓名为`dracarys`且姓名大于等于25岁的作者，且仅返回作者姓名、ID、年龄。

    /authors?select=id,age,name&name=like.dracarys&age=gte.25

查询名称名称为`Python`的书籍，且返回书籍ID、名称、书籍作者ID、作者名称。

    /books?select=id,name,author{id,name}&name=like.Python

查询作者姓名，年龄。返回第2页且分页数为10的数据，并按照ID降序排列。

    /authors?select=name,age&page=2&limit=10&order=id.desc

## 简单使用

### 定义模型
	
	class Author(UUIDBaseModel):
		"""
		作者
		"""
		id = PrimaryKeyField()
		name = CharField(max_length=50, unique=True)
		age = IntegerField(default=0)
		
		class Meta:
		    db_table = 'Author'
		
		def __repr__(self):
		    return u'<Author {}>'.format(self.name)

### 定义表单
	
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

### 定义视图
	
	class AuthorView(APIMethodView):
		"""
		作者视图
		"""
		model = Author
		paginate_by = 10
		context_object_name = 'items'
		pk_url_kwarg = 'author_id'
		form_class = AuthorForm

以上三步我们就基本实现了`Author`的基本增删改查了。

    > curl http://127.0.0.1:5000/authors
    {"status": {"message": "200 OK", "code": 0}, "data": {"count": 0, "items": [], "limit": 10, "page": 1, "max_page": 0}}
    # 查询年龄大于25的作者
    > curl http://127.0.0.1:5000/authors?age=gt.25
    # 查询姓名包含wwx的作者
    > curl http://127.0.0.1:5000/authors?name=like.wwx
    # 仅仅返回作者ID
    > curl http://127.0.0.1:5000/authors?select=id


## TODO

API文档。

## 联系

邮箱：`huiquanxiong@gmail.com`

## License

MIT
