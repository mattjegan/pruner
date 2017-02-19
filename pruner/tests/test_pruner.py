
import sys
import unittest

from mock import patch
import pytest

from pruner import Pruner, main

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

    def test_with_exit_code(self):
        args = [
            'pruner',
            '--with_exit_code',
            'pruner/tests/fake_proj/requirements.txt',
            'pruner/tests/fake_proj/output.txt',
            'python', 'pruner/tests/fake_proj/fake_proj.py'
        ]
        with self.assertRaises(SystemExit) as sysex:
            with patch.object(sys, 'argv', args):
                main()

        assert sysex.exception.code == 1

        with open('pruner/tests/fake_proj/output.txt') as f:
            topline = f.readline()
            assert topline.startswith('rancat') == True

    def test_nocolor(self):
        args = [
            'pruner',
            '--nocolor',
            'pruner/tests/fake_proj/requirements.txt',
            'pruner/tests/fake_proj/output.txt',
            'python', 'pruner/tests/fake_proj/fake_proj.py'
        ]
        try:
            with patch.object(sys, 'argv', args):
                p = Pruner()
                p.run()
        except:
            assert 1 == 0

        assert p.args.nocolor == True

    def test_initial_test_failure(self):
        args = [
            'pruner',
            'pruner/tests/fake_proj/requirements.txt',
            'pruner/tests/fake_proj/output.txt',
            'python', 'pruner/tests/fake_proj/fake_fail_proj.py'
        ]
        with self.assertRaises(SystemExit) as sysex:
            with patch.object(sys, 'argv', args):
                main()

        assert sysex.exception.code == 1

    def test_call_initial_without_list(self):
        args = [
            'pruner',
            '--nocolor',
            'pruner/tests/fake_proj/requirements.txt',
            'pruner/tests/fake_proj/output.txt',
            'python', 'pruner/tests/fake_proj/fake_proj.py'
        ]
        try:
            with patch.object(sys, 'argv', args):
                p = Pruner()
                s = p._call('ls', initial=True)
        except:
            assert 1 == 0

        assert s == 0