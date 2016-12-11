#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask_script import Manager
# dracarys import
from dracarys import create_app
from scripts.test import UnitTest
from scripts.syncdb import Syncdb

app = create_app()
manager = Manager(app)
manager.add_command('runtest', UnitTest())
manager.add_command('syncdb', Syncdb())


if __name__ == "__main__":
    manager.run()