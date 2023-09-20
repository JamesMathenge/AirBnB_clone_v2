#!/usr/bin/python3
"""A unit test module for the console (command interpreter).
"""
import unittest
from unittest.mock import patch
from console import HBNBCommand
import io
import sys


class TestConsoleCreate(unittest.TestCase):
    def setUp(self):
        self.cli = HBNBCommand()

    def tearDown(self):
        self.cli.do_destroy("State")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_with_params(self, mock_stdout):
        expected_output = "2b26e8dd-6765-445e-94b5-c416d7e237ef\n"
        with patch('builtins.input',
                   side_effect=['create State name="California"']):
            self.cli.onecmd("create State name='California'")
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_with_invalid_params(self, mock_stdout):
        expected_output = "** class name missing **\n"
        with patch('builtins.input',
                   side_effect=['create', 'create State',
                                'create State name="California']):
            self.cli.onecmd("create")
            self.cli.onecmd("create State")
            self.cli.onecmd("create State name=\"California")
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
