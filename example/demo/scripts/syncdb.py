#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask_script import Command
# dracarys import
from demo.scripts import create_tables


class Syncdb(Command):
    """
    同步数据库
    """
    command_name = 'syncdb'

    def run(self):
        create_tables()
        return
