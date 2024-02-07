#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO


class TestHBNBCommand(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def assert_output(self, expected_output, mock_stdout, function, *args):
        with patch('builtins.input', side_effect=args):
            TestHBNBCommand().onecmd(" ".join([function] + list(args)))
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_quit_command(self):
        self.assertTrue(self.assert_output('', 'quit'))

    def test_create_command(self):
        self.assert_output('** class name missing **', 'create')
        self.assert_output('** class doesn\'t exist **', 'create UnknownClass')
        self.assert_output('some_instance_id', 'create BaseModel')

    def test_show_command(self):
        self.assert_output('** class name missing **', 'show')
        self.assert_output('** instance id missing **', 'show BaseModel')
        self.assert_output('** no instance found **', 'show BaseModel instance_id_not_found')
        # Add more test cases as needed

    def test_destroy_command(self):
        # Similar to show command testing
        pass

    def test_all_command(self):
        # Similar to show command testing
        pass

    def test_update_command(self):
        # Similar to show command testing
        pass


if __name__ == '__main__':
    unittest.main()
