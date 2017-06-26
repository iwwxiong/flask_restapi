# Example

## Run

This demo require mysql service, so we must start mysql server(mysql config see `demo/config/default.py`). then wo can follow this.

    > source venv/bin/activate
    > pip install mysql-python
    > python manage.py syncdb
    > python manage.py runserver

Then we can view `http://127.0.0.1:5000` for test. The example contains `Book` and `Author` apps.

## Usage

### create

    > curl -d "name=wwx&age=20" http://127.0.0.1:5000/authors
    {"status": {"message": "200 OK", "code": 0}, "data": {"id": 1}}

### select

    > curl http://127.0.0.1:5000/authors/1?select=id,name
    {"status": {"message": "200 OK", "code": 0}, "data": {"name": "wwx", "id": 1}}

### update

    > curl -d "name=yyf" -H X_METHOD_OVERRIDE:PUT http://127.0.0.1:5000/authors/1
    {"status": {"message": "200 OK", "code": 0}, "data": {"id": 1}}

### delete

    > curl -H X_METHOD_OVERRIDE:DELETE http://127.0.0.1:5000/authors/1
    {"status": {"message": "delete success., "code": 0}, "data": []}

