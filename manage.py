#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'dracarysX'

from flask_script import Manager
# dracarys import
from dracarys import app

manager = Manager(app)

if __name__ == "__main__":
    manager.run()