#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask_script import Manager
# flask_restapi import
from demo import create_app
from demo.scripts.syncdb import Syncdb

app = create_app()
manager = Manager(app)
manager.add_command('syncdb', Syncdb())


if __name__ == "__main__":
    manager.run()
