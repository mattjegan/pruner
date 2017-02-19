
import sys
import unittest

from mock import patch
import pytest

from pruner import main

class TestRanCat(unittest.TestCase):
    def test_help(self):
        args = ['pruner', '--help']
        with self.assertRaises(SystemExit) as sysex:
            with patch.object(sys, 'argv', args):
                main()

        assert sysex.exception.code == 0