# Demo介绍

## 启动

    > python manage.py syncdb
    > python manage.py runserver

然后我们就可以直接访问`http://127.0.0.1:5000`。目前脚手架中间实现了`Book`和`Author`两个简单测试app。

## 使用

### 新增

    > curl -d "name=wwx&age=20" http://127.0.0.1:5000/authors
    {"status": {"message": "200 OK", "code": 0}, "data": {"id": 1}}

###　查询

    > curl http://127.0.0.1:5000/authors/1?select=id,name
    {"status": {"message": "200 OK", "code": 0}, "data": {"name": "wwx", "id": 1}}

### 修改

    > curl -d "name=yyf" -H X_METHOD_OVERRIDE:PUT http://127.0.0.1:5000/authors/1
    {"status": {"message": "200 OK", "code": 0}, "data": {"id": 1}}

### 删除

    > curl -H X_METHOD_OVERRIDE:DELETE http://127.0.0.1:5000/authors/1
    {"status": {"message": "delete success., "code": 0}, "data": []}

