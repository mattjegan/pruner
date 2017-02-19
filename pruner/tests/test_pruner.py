
import sys
import unittest

from mock import patch
import pytest

from pruner import main

class TestRanCat(unittest.TestCase):
    def test_help(self):
        args = [
            'pruner',
            '--help'
        ]
        with self.assertRaises(SystemExit) as sysex:
            with patch.object(sys, 'argv', args):
                main()

        assert sysex.exception.code == 0

    def test_full_run(self):
        args = [
            'pruner',
            'pruner/tests/fake_proj/requirements.txt',
            'pruner/tests/fake_proj/output.txt',
            'python', 'pruner/tests/fake_proj/fake_proj.py'
        ]
        try:
            with patch.object(sys, 'argv', args):
                main()
        except:
            assert 1 == 0

        with open('pruner/tests/fake_proj/output.txt') as f:
            topline = f.readline()
            assert topline.startswith('rancat') == True