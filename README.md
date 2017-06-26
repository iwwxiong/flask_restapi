# Flask rest api query framework

A simple rest query framework. Web framework use flask, orm by peewee, form by wtform and query by [rest_query](https://github.com/dracarysX/rest_query). The framework implements custom [query](https://postgrest.com) api(like this: /?select=id,name&id=gte.20), save form data, model object serializer, APIMethodView(get， post， put，delete) and errorhandler.

## Select API

`select id, name, age from Author where name = '%dracarysX' and age >= 25`

    curl http://localhost/authors?select=id,age,name&name=like.dracarys&age=gte.25

`select Book.id, Book.name, Author.id, Author.name from Book inner join Author on Book.author_id = Author.id where Book.id = 10`

    curl http://localhost/books?select=id,name,author{id,name}&id=10

`select id, name from Book order by id desc limit 1, 2`

    curl http://localhost/books?select=id,name&page=1&limit=2&order=id.desc

## Installing and Testing

For now, i did not push this package to public repository. so you can install by source code.

Use `virtualenv`:

    > git clone https://github.com/dracarysX/flask_restapi.git
    > cd flask_restapi
    > virtualenv --no-site-packages venv
    > source venv/bin/activate
    > python setup.py install
    > python setup.py test

## Usage

### declare model

```python
class Author(UUIDBaseModel):
	id = PrimaryKeyField()
	name = CharField(max_length=50, unique=True)
	age = IntegerField(default=0)
	
	class Meta:
		db_table = 'Author'
	
	def __repr__(self):
		return u'<Author {}>'.format(self.name)
```

### declare form

```python
class AuthorForm(PeeweeForm):
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
```

### declare view

```python
class AuthorView(APIMethodView):
	model = Author
	paginate_by = 10
	context_object_name = 'items'
	pk_url_kwarg = 'author_id'
	form_class = AuthorForm
```

After that we achieve create、update、select and delete for `Author`.

    > curl http://127.0.0.1:5000/authors
    {
		"status": {
			"message": "200 OK", 
			"code": 0
		}, 
		"data": {
			"count": 0, 
			"items": [], 
			"limit": 10, 
			"page": 1, 
			"max_page": 0
			}
		}
	}
    # select * from Author where age > 25
    > curl http://127.0.0.1:5000/authors?age=gt.25
    # select * from Author where name = '%wwx'
    > curl http://127.0.0.1:5000/authors?name=like.wwx
    # select id from Author
    > curl http://127.0.0.1:5000/authors?select=id

## Example

View [Example](https://github.com/dracarysX/flask_restapi/blob/master/example/README.md)


## Contact

Email: `huiquanxiong@gmail.com`

## License

MIT
