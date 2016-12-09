#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'dracarysX'

from flask_script import Manager
# dracarys import
from dracarys import create_app
from scripts.test import UnitTest

app = create_app()
manager = Manager(app)
manager.add_command('runtest', UnitTest())


if __name__ == "__main__":
    manager.run()