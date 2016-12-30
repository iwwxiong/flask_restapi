#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from flask_script import Command
# dracarys import
from tests.test_renders import *


class UnitTest(Command):
    """

    """
    command_name = 'runtest'

    def run(self):
        """Run unit tests."""
        tests = unittest.TestLoader().discover('tests', pattern='test_*.py')
        unittest.TextTestRunner(verbosity=1).run(tests)