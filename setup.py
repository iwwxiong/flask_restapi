#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys


class MyTest(TestCommand):
    """

    """
    def run_tests(self):
        tests = unittest.TestLoader().discover('tests', pattern='test_*.py')
        unittest.TextTestRunner(verbosity=1).run(tests)


if sys.version_info.major != 2 and sys.version_info.minor != 7:
    print("python version must be 2.7.x")
    sys.exit()


setup(
    name='flask_restapi',
    version='0.1.0',
    license='MIT',
    description=u'一款轻量的restAPI开发脚手架',
    author='dracarysX',
    author_email='huiquanxiong@gmail.com',
    url='https://github.com/dracarysX/flask_restapi',
    packages=find_packages(include=['flask_restapi']),
    install_requires=[
        'peewee',
        'flask',
        'wtforms',
        'flask_bcrypt',
        'flask-script'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Framework :: Flask',
        'Programming Language :: Python :: 2.7',
        'License :: MIT',
    ],
    keywords='Python, Flask, APIMethodView, Filtering Query API, Mysql, Peewee, RestAPI',
    long_description=u'一款简易的restapi开发脚手架。服务端采用flask，orm使用peewee，表单使用wtform。都是轻量级框架，'
                     u'简单易学。实现自定义查询查询API参考网站。实现表单保存，模型数据序列化，'
                     u'APIMethodView（实现get， post， put，delete操作），异常错误处理等。'
)
