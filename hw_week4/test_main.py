import unittest
from unittest.mock import patch
from main import valid_user

class TestValidUser(unittest.TestCase):
    @patch('main.input', return_value='user1')
    def test_valid_user_passes(self, mock_input):
        expected = 0
        result = valid_user()
        self.assertEqual(expected, result)
        self.assertEqual(mock_input.call_count, 1)

    @patch('main.input', return_value='blahh')
    def test_valid_user_fails(self, mock_input):
        with self.assertRaises(SystemExit) as context:
            valid_user()
        self.assertEqual(mock_input.call_count, 3)
        self.assertEqual(context.exception.code, 999)

if __name__ == '__main__':
    unittest.main()
